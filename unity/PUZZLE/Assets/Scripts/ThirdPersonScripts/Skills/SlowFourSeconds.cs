using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "SlowFourSeconds", menuName = "Skills/SlowFourSeconds")]
public class SlowFourSeconds : Skill
{
    public override void Activate(GameObject currentPlayer)
    {
        Time.timeScale = 0.02f;
    }
}
