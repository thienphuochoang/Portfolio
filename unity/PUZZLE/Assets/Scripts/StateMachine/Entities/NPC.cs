using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using System;

public class NPC : MonoBehaviour
{
    private StateMachine stateMachine;
    [Header("Wander Settings")]
    public bool isNPCsAssignedForWandering = false;
    public float wanderRadius = 15f;
    public float wanderTimer = 10f;
    [Header("Global Settings")]
    public List<AvailableStates> assignedOptionalStates = new List<AvailableStates>();
    public enum AvailableStates { CHASE }
    private AvailableStates availableStates;
    [Header("Walking Path Settings")]
    public List<Transform> pointList = new List<Transform>();
    [Header("Idle Settings")]
    public bool doesStepOnIdlePoint = false;
    [SerializeField]
    private float startDelay;
    [Header("Find-NPCs-to-talk settings")]
    public float findNPCRadius = 1.5f;
    public bool beAbleToTalk = false;
    public bool isTalking = false;
    public GameObject targetTalkingNPC;
    [Header("Player Detection Settings")]
    public bool isCallingForHelp = false;
    public bool doesReceiveHelp = false;
    public float receiveHelpFromOtherNPCsRange = 5f;
    public bool doesStartChasing = false;

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
        startDelay = UnityEngine.Random.Range(0.1f, 5f);
        var navMeshAgent = GetComponent<NavMeshAgent>();
        var anim = GetComponentInChildren<Animator>();
        stateMachine = new StateMachine();

        IState moveToPoint = new MoveToPoint(pointList, anim, this);
        IState idle = new Idle(this, anim);
        IState talk = new Talk(this, anim);
        IState alert = new Alert(this, anim);
        IState chase = new Chase(this, anim);
        IState wander = new Wander(this, anim, wanderRadius, wanderTimer);

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

        Func<bool> BeginToChase() => () =>
        {
            bool doesReceiveHelpFromOtherNPCs = GetNPCsForHelpInRange();
            if ((GetComponent<FindMonstersInRange>().redAlertPlayerTrigger == true && GetComponent<FindMonstersInRange>().canSeePlayer == true) || doesReceiveHelp == true)
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
        }
        else
        {
            GetComponent<FindMonstersInRange>().enabled = false;
        }
        
        
        if (isNPCsAssignedForWandering == true)
        {
            stateMachine.SetState(wander);
        }
        else
        {
            stateMachine.SetState(idle);
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
    }
    private void Start()
    {
        if (isNPCsAssignedForWandering == false)
        {
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
}