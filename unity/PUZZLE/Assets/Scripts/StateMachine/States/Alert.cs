using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Alert : IState
{
    private Animator _anim;
    private NPC _npc;
    private float timer = 0;
    private float clipLength;
    public Vector3 lastAgentVelocity;
    public Alert(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void OnEnter()
    {
        Pause();
        _npc.GetComponent<NavMeshAgent>().enabled = false;
        _npc.GetComponent<NavMeshObstacle>().enabled = true;
        
        AlertAnimation();
        clipLength = GetAlertAnimationClipLength();
        _npc.isCallingForHelp = true;
    }
    public void Tick()
    {
        timer += Time.deltaTime;
        if (timer > clipLength)
        {
            OnExit();
        }
    }
    public void OnExit()
    {
        timer = 0;
        _npc.GetComponent<NavMeshObstacle>().enabled = false;
        _npc.GetComponent<NavMeshAgent>().enabled = true;
        _npc.GetComponent<NPC>().doesStepOnIdlePoint = true;
        //_npc.GetComponent<FindMonstersInRange>().redAlertPlayerTrigger = false;
    }
    void AlertAnimation()
    {
        _anim.SetTrigger("AlertTrigger");
    }
    void Pause()
    {
        _npc.GetComponent<NavMeshAgent>().isStopped = true;
        //lastAgentVelocity = _npc.GetComponent<NavMeshAgent>().velocity;
        //lastAgentPath = _agent.path;
        //_npc.GetComponent<NavMeshAgent>().velocity = Vector3.zero;
        //_npc.GetComponent<NavMeshAgent>().isStopped = true;
        //_npc.GetComponent<NavMeshAgent>().updatePosition = false;
        //_npc.GetComponent<NavMeshAgent>().updateRotation = false;
        //_npc.GetComponent<NavMeshAgent>().ResetPath();
    }
    private float GetAlertAnimationClipLength()
    {
        float time = 0f;
        RuntimeAnimatorController ac = _anim.runtimeAnimatorController;    //Get Animator controller
        for (int i = 0; i < ac.animationClips.Length; i++)                 //For all animations
        {
            if (ac.animationClips[i].name == "Armed-Idle-Alert1")        //If it has the same name as your clip
            {
                time = ac.animationClips[i].length;
            }
        }
        return time;
    }
}