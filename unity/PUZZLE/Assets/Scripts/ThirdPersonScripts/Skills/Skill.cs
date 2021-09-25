using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using Sirenix.OdinInspector;
public class Skill : ScriptableObject
{
    public enum SkillState { READY, ACTIVE, COOLDOWN, NOTAVAILABLE };
    public SkillState state = SkillState.READY;
    public string skillName;
    public string spritePath;
    public bool isPassive;
    [EnableIf("@cameraEffect != null")]
    public string cameraEffect;
    [EnableIf("@isPassive == false")]
    public float activeTime;
    [EnableIf("@isPassive == false")]
    public float cooldownTime;
    [EnableIf("@isPassive == false")]
    public int availableTimes;
    public Dictionary<string, List<string>> skillDict = new Dictionary<string, List<string>>();
    public virtual void Activate(GameObject currentPlayer)
    {

    }
    public virtual void Ready(GameObject currentPlayer)
    {

    }
    public virtual void Cooldown(GameObject currentPlayer)
    {

    }
}
