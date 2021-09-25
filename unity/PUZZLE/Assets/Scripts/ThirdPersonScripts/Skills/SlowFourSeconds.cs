using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[CreateAssetMenu(fileName = "SlowFourSeconds", menuName = "Skills/SlowFourSeconds")]
public class SlowFourSeconds : Skill
{
    private float slowdownFactor = 0.05f;
    private float slowdownLength = 3f;
    private float originalActiveTime;
    private float originalCooldownTime;
    void test()
    {
        Time.timeScale += (1f / slowdownLength) * Time.unscaledDeltaTime;
        Time.timeScale = Mathf.Clamp(Time.timeScale, 0f, 1f);
    }
    private void StoreOriginalVariable()
    {
        originalActiveTime = activeTime;
        originalCooldownTime = cooldownTime;
    }
    private void MakeVariableBackToOriginalValue()
    {
        activeTime = originalActiveTime;
        cooldownTime = originalCooldownTime;
        Time.timeScale = 1f;
    }
    private void ActivateSlowMotion()
    {
        Time.timeScale = slowdownFactor;
        //Time.fixedDeltaTime = Time.timeScale * .02f;
    }
    private void EnableCameraBlurFocus()
    {
        
    }
    public override void Activate(GameObject currentPlayer)
    {
        ActivateSlowMotion();
    }
    public override void Ready(GameObject currentPlayer)
    {
        StoreOriginalVariable();
    }

    public override void Cooldown(GameObject currentPlayer)
    {
        MakeVariableBackToOriginalValue();
    }
}
