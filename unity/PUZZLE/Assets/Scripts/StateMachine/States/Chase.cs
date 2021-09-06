using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Chase : IState
{
    private Animator _anim;
    private NPC _npc;

    WaitForSecondsRealtime waitForSecondsRealtime;
    public float waitTime = 3;
    private float lastDistance;
    public Chase(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void OnEnter()
    {
        //Resume();
        _npc.isTalking = false;
        if (_npc.GetComponent<NPC>().doesReceiveHelp == true)
        { }
        ChaseAnimation();
        _npc.GetComponent<NavMeshAgent>().speed = 2.5f;
        _npc.isCallingForHelp = true;
        lastDistance = Vector3.Distance(_npc.GetComponent<FindMonstersInRange>().lastKnownLocation, _npc.transform.position);
    }
    public void Tick()
    {
        float currentDistance = Vector3.Distance(_npc.GetComponent<FindMonstersInRange>().lastKnownLocation, _npc.transform.position);
        if (_npc.GetComponent<FindMonstersInRange>().canSeePlayer == true)
        {
            _npc.GetComponent<NavMeshAgent>().destination = _npc.GetComponent<FindMonstersInRange>().lastKnownLocation;
        }
        else if (currentDistance < 0.5f)
        {
            OnExit();
        }
        // Check if npc stucks
        else if (lastDistance == currentDistance)
        {
            OnExit();
        }
        lastDistance = currentDistance;
    }
    public void OnExit()
    {
        //AlertAnimation();
        _npc.isTalking = false;
        _npc.beAbleToTalk = true;
        _npc.GetComponent<FindMonstersInRange>().redAlertPlayerTrigger = false;
        _npc.isCallingForHelp = false;
        _npc.GetComponent<NavMeshAgent>().speed = 1;
        _npc.GetComponent<NPC>().doesStepOnIdlePoint = true;
    }
    void ChaseAnimation()
    {
        _anim.SetTrigger("IdleWalkRunTrigger");
        _anim.SetFloat("Speed", 1);
    }
    void AlertAnimation()
    {
        _anim.SetTrigger("AlertTrigger");
    }
    IEnumerator WaitForNewLastKnownLocation()
    {
        Debug.Log("Start waiting: " + Time.realtimeSinceStartup);

        if (waitForSecondsRealtime == null)
            waitForSecondsRealtime = new WaitForSecondsRealtime(waitTime);
        else
            waitForSecondsRealtime.waitTime = waitTime;
        yield return waitForSecondsRealtime;

        Debug.Log("End waiting: " + Time.realtimeSinceStartup);
    }
}
