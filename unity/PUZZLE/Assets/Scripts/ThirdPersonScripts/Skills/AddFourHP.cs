using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "AddFourHP", menuName = "Skills/AddFourHP")]
public class AddFourHP : Skill
{
    private string functionName = "AddFourHP";
    public override bool AssignSkillAttributesFromDatabase()
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
            return true;
        }
        return false;
    }
    public override void Activate(GameObject currentPlayer)
    {
        bool IsFoundData = AssignSkillAttributesFromDatabase();
        if (IsFoundData == true)
        {
            currentPlayer.GetComponent<PlayerAttributes>().defaultHP = 9;
        }
    }
}
