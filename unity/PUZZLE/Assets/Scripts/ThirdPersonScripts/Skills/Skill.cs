using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
public class Skill : ScriptableObject
{
    public string skillName;
    public string spritePath;
    public bool isPassive;
    public float activeTime;
    public float cooldownTime;
    public float availableTime;
    public Dictionary<string, List<string>> skillDict = new Dictionary<string, List<string>>();
    public virtual void Activate()
    {

    }
    private void OnEnable()
    {
        skillDict = FindObjectOfType<SkillAttributes>().skillDict;
    }
    public virtual void AssignSkillAttributesFromDatabase()
    {
    }
}
