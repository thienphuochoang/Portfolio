using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
public class Attack : IState
{
    private Animator _anim;
    private NPC _npc;
    public Attack(NPC npc, Animator anim)
    {
        _npc = npc;
        _anim = anim;
    }
    public void OnEnter()
    {
    }
    public void Tick()
    {
        if (_npc.GetComponent<NPC>().DoesPlayerInAttackRange() == true)
        {
            if (_anim.GetCurrentAnimatorStateInfo(0).normalizedTime > 1)
            {
                AttackAnimation();
            }
        }
        else
        {
            OnExit();
        }
    }
    public void OnExit()
    {
        _npc.isTalking = false;
        _npc.beAbleToTalk = true;
        //_npc.GetComponent<FindMonstersInRange>().redAlertPlayerTrigger = false;
        //_npc.isCallingForHelp = false;
        _npc.GetComponent<NPC>().doesStepOnIdlePoint = true;
    }
    private void AttackAnimation()
    {
        _anim.SetTrigger("AttackTrigger");
    }
    private void Hit() => _npc.GetComponentInChildren<AnimationEventScripts>().Hit();
}
