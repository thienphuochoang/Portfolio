using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Talk : IState
{
    private Animator _anim;
    private NPC _npc;
    private float randomTime = Random.Range(8f, 10f);
    private float timer;
    private Vector3 lastAgentVelocity;
    public Talk(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void OnEnter()
    {
        _npc.GetComponent<NavMeshAgent>().enabled = false;
        _npc.GetComponent<NavMeshObstacle>().enabled = true;
        TalkingAnimation();
        Pause();
        _npc.beAbleToTalk = false;
        _npc.doesStepOnIdlePoint = true;
        timer = 0f;
        _npc.transform.LookAt(_npc.targetTalkingNPC.transform.position);
    }
    public void Tick()
    {
        // Make sure that BeAbleToTalk variable is always different from IsTalking variable
        if (_npc.isTalking == true)
            _npc.beAbleToTalk = false;
        else
            _npc.beAbleToTalk = true;
        TalkingAnimation();

        // Cancel talking based on random time
        timer += Time.deltaTime;

        if (timer > randomTime)
        {
            OnExit();
        }
    }
    public void OnExit()
    {
        _npc.GetComponent<NavMeshObstacle>().enabled = false;
        _npc.GetComponent<NavMeshAgent>().enabled = true;
        _npc.isTalking = false;
        _npc.beAbleToTalk = true;
        _npc.doesStepOnIdlePoint = false;
        _npc.targetTalkingNPC = null;
        _anim.SetTrigger("IdleWalkTrigger");
        Resume();

    }
    void TalkingAnimation()
    {
        _anim.SetTrigger("Talking1Trigger");
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
