using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using System;

public class NPC : MonoBehaviour
{
    private StateMachine stateMachine;
    [Header("Walking Path Settings")]
    public List<Transform> pointList = new List<Transform>();
    [Header("Idle Settings")]
    public bool doesStepOnIdlePoint = false;
    public bool foundOtherNPCIdling = false;
    [SerializeField]
    private float startDelay;
    [Header("Find-NPCs-to-talk settings")]
    public float findNPCRadius = 1.5f;
    public bool beAbleToTalk = false;
    public bool isTalking = false;
    public GameObject targetTalkingNPC;

    private void Awake()
    {
        startDelay = UnityEngine.Random.Range(0.1f, 5f);
        var navMeshAgent = GetComponent<NavMeshAgent>();
        var anim = GetComponentInChildren<Animator>();
        var navMeshObstacle = GetComponent<NavMeshObstacle>();
        stateMachine = new StateMachine();

        IState moveToPoint = new MoveToPoint(pointList, anim, this);
        IState idle = new Idle(this, anim);
        IState talk = new Talk(this, anim);

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

        stateMachine.SetState(moveToPoint);
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
    void Update() => stateMachine.Tick();
    private void Start()
    {
        Invoke(nameof(IdleRandomly), startDelay);
    }


    void IdleRandomly()
    {
        float spawnInterval = UnityEngine.Random.Range(20f, 30f);
        doesStepOnIdlePoint = true;
        Invoke(nameof(IdleRandomly), spawnInterval);
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
}