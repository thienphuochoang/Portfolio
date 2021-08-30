using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimationEventScripts : MonoBehaviour
{
    private Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        anim = this.GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    //Placeholder functions for Animation events
    public void Hit() { }
    public void Shoot() { }
    public void FootR() { }
    public void FootL() { }
    public void Land() { }
    public void WeaponSwitch() { }
}
