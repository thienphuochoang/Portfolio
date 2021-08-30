using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LookAt : IState
{
    private PerfectLookAt _perfectLookAtFeatures;
    private float time;
    public event EventHandler OnTriggerLook;
    public LookAt(PerfectLookAt perfectLookAtFeatures)
    {
        _perfectLookAtFeatures = perfectLookAtFeatures;
        // _peasant = peasant;
    }
    public void OnEnter()
    {
        //_perfectLookAtFeatures.LookAtObject();
    }
    public void Tick()
    {
        //_perfectLookAtFeatures.LookAtObject();
    }
    public void OnExit()
    {

    }
    IEnumerator WaitThenLook()
    {
        yield return new WaitForSeconds(5);
        //_perfectLookAtFeatures.LookAtObject();
    }
}
