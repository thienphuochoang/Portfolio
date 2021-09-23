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
    [EnableIf("@isPassive == false")]
    public float activeTime;
    [EnableIf("@isPassive == false")]
    public float cooldownTime;
    [EnableIf("@isPassive == false")]
    public float availableTime;
    public Dictionary<string, List<string>> skillDict = new Dictionary<string, List<string>>();
    public virtual void Activate(GameObject currentPlayer)
    {

    }
}
