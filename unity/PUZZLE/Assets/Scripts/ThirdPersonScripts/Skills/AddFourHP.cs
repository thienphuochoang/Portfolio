using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "AddFourHP", menuName = "Skills/AddFourHP")]
public class AddFourHP : Skill
{
    private string functionName = "AddFourHP";
    private bool didFindDataFromSkillDatabase = false;
    private void OnEnable()
    {
        AssignSkillAttributesFromDatabase();
    }
    public override void AssignSkillAttributesFromDatabase()
    {
        if (skillDict.ContainsKey(functionName))
        {
            skillName = skillDict[functionName][0];
            spritePath = skillDict[functionName][2];
            if (skillDict[functionName][3].Contains("Yes"))
                isPassive = true;
            else
                isPassive = false;
            activeTime = float.Parse(skillDict[functionName][4]);
            didFindDataFromSkillDatabase = true;
        }
    }
    public override void Activate()
    {
        if (didFindDataFromSkillDatabase == true)
        {
            Debug.Log("ahihi");
        }
    }
}
