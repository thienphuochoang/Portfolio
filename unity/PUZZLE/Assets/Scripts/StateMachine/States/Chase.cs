using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Chase : IState
{
    private Animator _anim;
    private NPC _npc;

    public float waitTime = 3;
    private float lastDistance;
    private Vector3 _desVelocity;
    public float _speed = 2.5f;
    public float _turnSpeed = 2;
    public Chase(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void OnEnter()
    {
        //Resume();
        //if (_doesHaveWeapon == true)
        //{
        //    Pause();
        //    clipLength = GetWeaponAnimationClipLength();
        //    UnsheatheWeapon();
        //}
        _npc.isTalking = false;
        //ChaseAnimation();
        _npc.GetComponent<NavMeshAgent>().speed = 2.5f;
        _npc.isCallingForHelp = true;
        lastDistance = Vector3.Distance(_npc.GetComponent<FindMonstersInRange>().lastKnownLocation, _npc.transform.position);
    }
    public void Tick()
    {
        ChaseAnimation();
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
        
        //else
        //{
        /*
        ChaseAnimation();
        float currentDistance = Vector3.Distance(_npc.GetComponent<FindMonstersInRange>().lastKnownLocation, _npc.transform.position);
        if (_npc.GetComponent<FindMonstersInRange>().canSeePlayer == true)
        {
            //_npc.GetComponent<NavMeshAgent>().destination = _npc.GetComponent<FindMonstersInRange>().lastKnownLocation;
            Vector3 lookPos;
            Quaternion targetRot;

            _npc.GetComponent<NavMeshAgent>().destination = _npc.GetComponent<FindMonstersInRange>().lastKnownLocation;
            _desVelocity = _npc.GetComponent<NavMeshAgent>().desiredVelocity;

            _npc.GetComponent<NavMeshAgent>().updatePosition = false;
            _npc.GetComponent<NavMeshAgent>().updateRotation = false;

            lookPos = _npc.GetComponent<FindMonstersInRange>().lastKnownLocation - _npc.transform.position;
            lookPos.y = 0;
            targetRot = Quaternion.LookRotation(lookPos);
            _npc.transform.rotation = Quaternion.Slerp(_npc.transform.rotation, targetRot, Time.deltaTime * _turnSpeed);

            _npc.GetComponent<CharacterController>().Move(_desVelocity.normalized * _speed * Time.deltaTime);

            _npc.GetComponent<NavMeshAgent>().velocity = _npc.GetComponent<CharacterController>().velocity;
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
        //}
        */
    }
    public void OnExit()
    {
        //AlertAnimation();
        _npc.GetComponent<NavMeshAgent>().speed = 1;
        if (_npc.GetComponent<NPC>().DoesPlayerInAttackRange() == false)
        {
            _npc.isTalking = false;
            _npc.beAbleToTalk = true;
            _npc.GetComponent<FindMonstersInRange>().redAlertPlayerTrigger = false;
            _npc.isCallingForHelp = false;
            _npc.GetComponent<NPC>().doesStepOnIdlePoint = true;
        }  
    }
    void ChaseAnimation()
    {
        _anim.SetTrigger("IdleWalkRunTrigger");
        _anim.SetFloat("Speed", 1);
    }
    private void UnsheatheWeapon()
    {
        _anim.SetTrigger("UnsheatheSword");
    }
    private void IdleAnimation()
    {
        _anim.SetTrigger("IdleWalkRunTrigger");
        _anim.SetFloat("Speed", 0);
    }
    private float GetWeaponAnimationClipLength()
    {
        float time = 0f;
        RuntimeAnimatorController ac = _anim.runtimeAnimatorController;    //Get Animator controller
        for (int i = 0; i < ac.animationClips.Length; i++)                 //For all animations
        {
            if (ac.animationClips[i].name == "Unsheath-L-Back")        //If it has the same name as your clip
            {
                time = ac.animationClips[i].length;
            }
        }
        return time;
    }
    void Pause()
    {
        //lastAgentVelocity = _npc.GetComponent<NavMeshAgent>().velocity;
        //lastAgentPath = _agent.path;
        //_npc.GetComponent<NavMeshAgent>().velocity = Vector3.zero;
        _npc.GetComponent<NavMeshAgent>().isStopped = true;
        //_npc.GetComponent<NavMeshAgent>().updatePosition = false;
        //_npc.GetComponent<NavMeshAgent>().updateRotation = false;
        //_npc.GetComponent<NavMeshAgent>().ResetPath();
    }
    void Resume()
    {
        //WalkingAnimation();
        //_npc.GetComponent<NavMeshAgent>().updatePosition = true;
        //_npc.GetComponent<NavMeshAgent>().updateRotation = true;
        _npc.GetComponent<NavMeshAgent>().isStopped = false;
        //_npc.GetComponent<NavMeshAgent>().velocity = lastAgentVelocity;
        //_agent.SetPath(lastAgentPath);
    }
}
