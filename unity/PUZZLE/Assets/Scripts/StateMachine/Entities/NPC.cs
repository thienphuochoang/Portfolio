using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using System;

public class NPC : MonoBehaviour
{
    private StateMachine stateMachine;
    public enum OnlyOneStateAssigned { NOT_AVAILABLE, IDLE, WANDER }
    public OnlyOneStateAssigned onlyOneStateAssigned;
    [Header("Wander Settings")]
    public float wanderRadius = 15f;
    public float wanderTimer = 10f;
    [Header("Global Settings")]
    public List<AvailableStates> assignedOptionalStates = new List<AvailableStates>();
    public enum AvailableStates { CHASE, HAVE_WEAPON }
    private AvailableStates availableStates;
    [Header("Walking Path Settings")]
    public List<Transform> pointList = new List<Transform>();
    [Header("Idle Settings")]
    public bool doesStepOnIdlePoint = false;
    private float startDelay;
    [Header("Find-NPCs-to-talk settings")]
    public float findNPCRadius = 2f;
    public bool beAbleToTalk = false;
    public bool isTalking = false;
    public GameObject targetTalkingNPC;
    [Header("Player Detection Settings")]
    public bool isCallingForHelp = false;
    public bool doesReceiveHelp = false;
    public float receiveHelpFromOtherNPCsRange = 5f;
    public bool doesStartChasing = false;
    [Header("Attack Settings")]
    public float attackRange = 2f;

    private void Awake()
    {
        bool chaseStateAvailable = false;
        foreach (var assignedState in assignedOptionalStates)
        {
            if (assignedState == AvailableStates.CHASE)
            {
                chaseStateAvailable = true;
            }
        }
        var navMeshAgent = GetComponent<NavMeshAgent>();
        var anim = GetComponentInChildren<Animator>();
        stateMachine = new StateMachine();

        IState moveToPoint = new MoveToPoint(pointList, anim, this);
        IState idle = new Idle(this, anim);
        IState talk = new Talk(this, anim);
        IState alert = new Alert(this, anim);
        IState chase = new Chase(this, anim);
        IState wander = new Wander(this, anim, wanderRadius, wanderTimer);
        IState attack = new Attack(this, anim);

        void At(IState to, IState from, Func<bool> condition) => stateMachine.AddTransition(to, from, condition);

        At(moveToPoint, idle, StepOnIdlePoint());
        At(idle, moveToPoint, ContinueWalking());
        At(idle, talk, BeginToTalk());
        At(talk, moveToPoint, ContinueWalking());
        

        Func<bool> StepOnIdlePoint() => () => doesStepOnIdlePoint == true;
        Func<bool> ContinueWalking() => () => doesStepOnIdlePoint == false && isTalking == false;
        Func<bool> BeginToTalk() => () =>
        {
            targetTalkingNPC = GetNPCsInRange();
            if (targetTalkingNPC != null && targetTalkingNPC.GetComponent<NPC>().stateMachine.CurrentState is Idle)
            {
                targetTalkingNPC.GetComponent<NPC>().isTalking = true;
                return true;
            }
            else if (targetTalkingNPC != null && isTalking == true)
            {
                targetTalkingNPC.GetComponent<NPC>().isTalking = true;
                return true;
            }
            else
                return false;
        };

        Func<bool> BeginToAttack() => () =>
        {
            bool doesPlayerInAttackRange = DoesPlayerInAttackRange();
            if (GetComponent<FindMonstersInRange>().redAlertPlayerTrigger == true && doesPlayerInAttackRange == true)
            {
                return true;
            }
            else
                return false;
        };

        Func<bool> BeginToChase() => () =>
        {
            bool doesReceiveHelpFromOtherNPCs = GetNPCsForHelpInRange();
            bool doesPlayerInAttackRange = DoesPlayerInAttackRange();
            if ((GetComponent<FindMonstersInRange>().redAlertPlayerTrigger == true && GetComponent<FindMonstersInRange>().canSeePlayer == true && !(stateMachine.CurrentState is Chase)) && doesPlayerInAttackRange == false || doesReceiveHelp == true)
            {
                return true;
            }
            else
                return false;
        };
        
        if (chaseStateAvailable == true)
        {
            GetComponent<FindMonstersInRange>().enabled = true;
            stateMachine.AddAnyTransition(chase, BeginToChase());
            At(chase, idle, StepOnIdlePoint());
            At(chase, attack, BeginToAttack());
            At(attack, idle, StepOnIdlePoint());
            //stateMachine.AddAnyTransition(attack, BeginToAttack());
        }
        else if (chaseStateAvailable == false)
        {
            GetComponent<FindMonstersInRange>().enabled = false;
        }

        
        if (onlyOneStateAssigned == OnlyOneStateAssigned.WANDER)
        {
            stateMachine.SetState(wander);
        }
        else if (onlyOneStateAssigned == OnlyOneStateAssigned.NOT_AVAILABLE || onlyOneStateAssigned == OnlyOneStateAssigned.IDLE)
        {
            stateMachine.SetState(idle);
            doesStepOnIdlePoint = true;
        }
        
        /*
        var navMeshAgent = GetComponent<NavMeshAgent>();
        var animator = GetComponent<Animator>();
        var enemyDetector = gameObject.AddComponent<EnemyDetector>();
        var fleeParticleSystem = gameObject.GetComponentInChildren<ParticleSystem>();

        _stateMachine = new StateMachine();

        var search = new SearchForResource(this);
        var moveToSelected = new MoveToSelectedResource(this, navMeshAgent, animator);
        var harvest = new HarvestResource(this, animator);
        var returnToStockpile = new ReturnToStockpile(this, navMeshAgent, animator);
        var placeResourcesInStockpile = new PlaceResourcesInStockpile(this);
        var flee = new Flee(this, navMeshAgent, enemyDetector, animator, fleeParticleSystem);

        At(search, moveToSelected, HasTarget());
        At(moveToSelected, search, StuckForOverASecond());
        At(moveToSelected, harvest, ReachedResource());
        At(harvest, search, TargetIsDepletedAndICanCarryMore());
        At(harvest, returnToStockpile, InventoryFull());
        At(returnToStockpile, placeResourcesInStockpile, ReachedStockpile());
        At(placeResourcesInStockpile, search, () => _gathered == 0);

        _stateMachine.AddAnyTransition(flee, () => enemyDetector.EnemyInRange);
        At(flee, search, () => enemyDetector.EnemyInRange == false);

        _stateMachine.SetState(search);

        void At(IState to, IState from, Func<bool> condition) => _stateMachine.AddTransition(to, from, condition);
        Func<bool> HasTarget() => () => Target != null;
        Func<bool> StuckForOverASecond() => () => moveToSelected.TimeStuck > 1f;
        Func<bool> ReachedResource() => () => Target != null &&
                                              Vector3.Distance(transform.position, Target.transform.position) < 1f;

        Func<bool> TargetIsDepletedAndICanCarryMore() => () => (Target == null || Target.IsDepleted) && !InventoryFull().Invoke();
        Func<bool> InventoryFull() => () => _gathered >= _maxCarried;
        Func<bool> ReachedStockpile() => () => StockPile != null &&
                                               Vector3.Distance(transform.position, StockPile.transform.position) < 1f;
        */
    }
    /*
    bool IsObjectInRange()
    {
        float distance = Vector3.Distance(this.GetComponent<PerfectLookAt>().m_TargetObject.transform.position, this.transform.position);
        if (distance < 1.0f)
            return true;
        else
            return false;
    }
    */
    //void Update() => stateMachine.Tick();
    void Update()
    {
        stateMachine.Tick();
        //Debug.Log(stateMachine.CurrentState);
    }
    private void Start()
    {
        if (onlyOneStateAssigned == OnlyOneStateAssigned.NOT_AVAILABLE)
        {
            startDelay = UnityEngine.Random.Range(0.1f, 5f);
            Invoke(nameof(IdleRandomly), startDelay);
        }
    }


    void IdleRandomly()
    {
        if (GetComponent<FindMonstersInRange>().redAlertPlayerTrigger == false)
        {
            float spawnInterval = UnityEngine.Random.Range(20f, 30f);
            doesStepOnIdlePoint = true;
            Invoke(nameof(IdleRandomly), spawnInterval);
        }

    }
    public GameObject GetNPCsInRange()
    {
        GameObject targetTalkingNPC;
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, findNPCRadius);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.gameObject.tag.Contains("NPC") && hitCollider.gameObject.name != transform.name)
            {
                targetTalkingNPC = hitCollider.gameObject;
                return targetTalkingNPC;
            }
        }
        return null;
    }
    public bool GetNPCsForHelpInRange()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, receiveHelpFromOtherNPCsRange);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.gameObject.tag.Contains("NPC") && hitCollider.gameObject.name != transform.name && hitCollider.GetComponent<NPC>().isCallingForHelp == true)
            {
                return true;
            }
        }
        return false;
    }
    public bool DoesPlayerInAttackRange()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, attackRange);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.gameObject.tag.Contains("Controller"))
            {
                return true;
            }
        }
        return false;
    }
    public GameObject GetPlayerInAttackRange()
    {
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, attackRange);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.gameObject.tag.Contains("Controller"))
            {
                return hitCollider.gameObject;
            }
        }
        return null;
    }
    public void OnCollisionEnter(Collision collision)
    {
        Debug.Log(collision.gameObject.name);
        //AddHitEffect(collision.GetContact(0).point, characterCamera.transform.rotation);
    }
}