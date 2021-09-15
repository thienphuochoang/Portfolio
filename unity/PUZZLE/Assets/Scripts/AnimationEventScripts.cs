using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimationEventScripts : MonoBehaviour
{
    private Animator anim;
    private GameObject player;
    public Transform handTransform;
    private GeneralParticleFeatures particleFeatures;
    // Start is called before the first frame update
    void Start()
    {
        anim = this.GetComponent<Animator>();
        particleFeatures = FindObjectOfType<GeneralParticleFeatures>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    //Placeholder functions for Animation events
    public GameObject Hit()
    {
        if (GetComponentInParent<NPC>().DoesPlayerInAttackRange() == true)
        {
            player = GetComponentInParent<NPC>().GetPlayerInAttackRange();
            GameObject hitEffectParticle = particleFeatures.AddHitEffect(handTransform.position, Camera.current.transform.rotation);
            hitEffectParticle.transform.localEulerAngles = new Vector3(0.3f, 0.3f, 0.3f);
            player.GetComponent<PlayerAttributes>().attributes._health -= 1;
        }
        return null;
    }
    
    public void Shoot() { }
    public void FootR() { }
    public void FootL() { }
    public void Land() { }
    public void WeaponSwitch() { }

}
