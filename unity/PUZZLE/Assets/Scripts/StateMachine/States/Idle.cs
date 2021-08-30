using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Idle : IState
{
    private NPC _npc;
    private Animator _anim;
    private Vector3 lastAgentVelocity;
    private float randomTime = Random.Range(5f, 10f);
    private float timer;

    public Idle(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void Tick()
    {
        //if (_doesStepOnIdlePoint == true)
        //{
        //    Pause();
        //    IdleAnimation();
        //}

        timer += Time.deltaTime;

        if (timer > randomTime)
        {
            OnExit();
        }
    }


    public void OnEnter()
    {
        _npc.GetComponent<NavMeshAgent>().enabled = false;
        _npc.GetComponent<NavMeshObstacle>().enabled = true;
        timer = 0f;
        Pause();
        IdleAnimation();
        _npc.beAbleToTalk = true;
    }
    public void OnExit()
    {
        _npc.doesStepOnIdlePoint = false;
        _npc.GetComponent<NavMeshObstacle>().enabled = false;
        _npc.GetComponent<NavMeshAgent>().enabled = true;
        Resume();
        //Resume();
        //WalkingAnimation();
        //if (_doesStepOnIdlePoint == false)
        //{
        //    ResumeRandomly();
        //}
    }

    void IdleAnimation()
    {
        _anim.SetFloat("Speed", 0);
    }

    void Pause()
    {
        lastAgentVelocity = _npc.GetComponent<NavMeshAgent>().velocity;
        //lastAgentPath = _agent.path;
        _npc.GetComponent<NavMeshAgent>().velocity = Vector3.zero;
        //_npc.GetComponent<NavMeshAgent>().isStopped = true;
        _npc.GetComponent<NavMeshAgent>().updatePosition = false;
        _npc.GetComponent<NavMeshAgent>().updateRotation = false;
        //_npc.GetComponent<NavMeshAgent>().ResetPath();
    }
    void Resume()
    {
        //WalkingAnimation();
        _npc.GetComponent<NavMeshAgent>().updatePosition = true;
        _npc.GetComponent<NavMeshAgent>().updateRotation = true;
        _npc.GetComponent<NavMeshAgent>().isStopped = false;
        _npc.GetComponent<NavMeshAgent>().velocity = lastAgentVelocity;
        //_agent.SetPath(lastAgentPath);
    }
}
