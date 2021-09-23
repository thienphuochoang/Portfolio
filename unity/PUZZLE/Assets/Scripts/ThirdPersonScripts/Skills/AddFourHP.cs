using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "AddFourHP", menuName = "Skills/AddFourHP")]
public class AddFourHP : Skill
{
    public override void Activate(GameObject currentPlayer)
    {
        currentPlayer.GetComponent<PlayerAttributes>().attributes._health += 4;
    }
}
