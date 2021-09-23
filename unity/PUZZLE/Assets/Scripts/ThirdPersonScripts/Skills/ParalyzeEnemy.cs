using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "ParalyzeEnemy", menuName = "Skills/ParalyzeEnemy")]
public class ParalyzeEnemy : Skill
{
    public override void Activate(GameObject currentPlayer)
    {
        Debug.Log("Paralyze skill activated!!!");
    }
}
