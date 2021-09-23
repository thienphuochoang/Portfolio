using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "AddFourMana", menuName = "Skills/AddFourMana")]
public class AddFourMana : Skill
{
    public override void Activate(GameObject currentPlayer)
    {
        currentPlayer.GetComponent<PlayerAttributes>().attributes._mana += 4;
    }
}
