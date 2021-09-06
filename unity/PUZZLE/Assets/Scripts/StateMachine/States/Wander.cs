using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Wander : IState
{
    public float _wanderRadius;
    public float _wanderTimer;
    private float randomTime = Random.Range(5f, 10f);
    private float idleTime;

    private float lastDistance;
    private Vector3 newPos;
    private Animator _anim;
    private NPC _npc;
    private float timer;

    public Wander(NPC npc, Animator anim, float wanderRadius, float wanderTimer)
    {
        _anim = anim;
        _npc = npc;
        _wanderRadius = wanderRadius;
        _wanderTimer = wanderTimer;
    }
    public void OnEnter()
    {
        timer = _wanderTimer;
        lastDistance = Vector3.Distance(newPos, _npc.transform.position);
    }

    public void Tick()
    {
        float currentDistance = Vector3.Distance(newPos, _npc.transform.position);
        timer += Time.deltaTime;

        if (timer >= _wanderTimer)
        {
            WalkingAnimation();
            Resume();
            newPos = RandomNavSphere(_npc.transform.position, _wanderRadius, -1);
            bool canReach = CanReachPosition(newPos, _npc.GetComponent<NavMeshAgent>());
            if (canReach == true)
                _npc.GetComponent<NavMeshAgent>().SetDestination(newPos);
            timer = 0;
        }
        else if (currentDistance < 0.1f)
        {
            IdleAnimation();
            Pause();
            idleTime += Time.deltaTime;
            if (idleTime >= randomTime)
            {
                WalkingAnimation();
                Resume();
                newPos = RandomNavSphere(_npc.transform.position, _wanderRadius, -1);
                bool canReach = CanReachPosition(newPos, _npc.GetComponent<NavMeshAgent>());
                if (canReach == true)
                    _npc.GetComponent<NavMeshAgent>().SetDestination(newPos);
                else
                    newPos = RandomNavSphere(_npc.transform.position, _wanderRadius, -1);
                idleTime = 0f;
            }

            timer = 0;
        }
        // Check if npc stucks
        else if (lastDistance == currentDistance)
        {
            IdleAnimation();
            Pause();
            idleTime += Time.deltaTime;
            if (idleTime >= randomTime)
            {
                WalkingAnimation();
                Resume();
                newPos = RandomNavSphere(_npc.transform.position, _wanderRadius, -1);
                bool canReach = CanReachPosition(newPos, _npc.GetComponent<NavMeshAgent>());
                if (canReach == true)
                    _npc.GetComponent<NavMeshAgent>().SetDestination(newPos);
                else
                    newPos = RandomNavSphere(_npc.transform.position, _wanderRadius, -1);
                idleTime = 0f;
            }

            timer = 0;
        }
        
        lastDistance = currentDistance;
    }

    public void OnExit()
    {

    }
    private Vector3 RandomNavSphere(Vector3 origin, float dist, int layermask)
    {
        Vector3 randDirection = Random.insideUnitSphere * dist;

        randDirection += origin;

        NavMeshHit navHit;

        NavMesh.SamplePosition(randDirection, out navHit, dist, layermask);

        return navHit.position;
    }
    void WalkingAnimation()
    {
        _anim.SetFloat("Speed", 0.5f);
    }
    void IdleAnimation()
    {
        _anim.SetFloat("Speed", 0f);
    }
    void Pause()
    {
        _npc.GetComponent<NavMeshAgent>().isStopped = true;
        //_npc.GetComponent<NavMeshAgent>().velocity = Vector3.zero;
        //_npc.GetComponent<NavMeshAgent>().updatePosition = false;
        //_npc.GetComponent<NavMeshAgent>().updateRotation = false;
    }
    void Resume()
    {
        _npc.GetComponent<NavMeshAgent>().isStopped = false;
        //_npc.GetComponent<NavMeshAgent>().velocity = Vector3.zero;
        //_npc.GetComponent<NavMeshAgent>().updatePosition = false;
        //_npc.GetComponent<NavMeshAgent>().updateRotation = false;
    }
    private bool CanReachPosition(Vector3 position, NavMeshAgent npcAgent)
    {
        NavMeshPath path = new NavMeshPath();
        npcAgent.CalculatePath(position, path);
        return path.status == NavMeshPathStatus.PathComplete;
    }
}
