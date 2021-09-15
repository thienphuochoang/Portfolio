using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unsheathe : IState
{
    private NPC _npc;
    private Animator _anim;
    private Transform _weaponHolder;
    private Transform _weaponAtTheBack;
    private float clipLength;
    private float timer;
    public Unsheathe(NPC npc, Animator anim, Transform weaponHolder, Transform weaponAtTheBack)
    {
        _npc = npc;
        _anim = anim;
        _weaponHolder = weaponHolder;
        _weaponAtTheBack = weaponAtTheBack;
    }
    public void OnEnter()
    {
        clipLength = GetWeaponAnimationClipLength();
        UnsheatheWeapon();
    }
    public void Tick()
    {
        timer += Time.deltaTime;

        if (timer > 0.5f && timer < clipLength)
        {
            _weaponHolder.gameObject.SetActive(true);
            _weaponAtTheBack.gameObject.SetActive(false);
        }
        if (timer > clipLength)
        {
            OnExit();
        }
    }
    public void OnExit()
    {
        timer = 0;
    }
    private void UnsheatheWeapon()
    {
        _anim.SetTrigger("UnsheatheSword");
    }
    private float GetWeaponAnimationClipLength()
    {
        float time = 0f;
        RuntimeAnimatorController ac = _anim.runtimeAnimatorController;    //Get Animator controller
        for (int i = 0; i < ac.animationClips.Length; i++)                 //For all animations
        {
            if (ac.animationClips[i].name == "Unarmed-Unsheath-R-Back")        //If it has the same name as your clip
            {
                time = ac.animationClips[i].length;
            }
        }
        return time;
    }
}
