using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DetectCollisionImpact : MonoBehaviour
{
    private GeneralParticleFeatures AddParticleClass;
    private float maximumKineticEnergy = 0.1f;
    //private PickUpAndThrowObjects PickUpAndThrowObjectsClass;
    // Start is called before the first frame update
    void Start()
    {
        AddParticleClass = FindObjectOfType<GeneralParticleFeatures>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void OnCollisionEnter(Collision collision)
    {
        float kineticEnergy = calculateKineticEnergy(this.GetComponent<Rigidbody>().mass, this.GetComponent<Rigidbody>().velocity.magnitude);
        float convertedKineticEnergy = convertKineticEnergyBasedOnMaximumAllowedNumber(kineticEnergy);
        try
        {
            GameObject loadedPrefab = AddParticleClass.loadParticleFromPrefab("FX/Cartoon FX/CFX Prefabs/Misc/" + "CFX_Poof");
            GameObject particle = AddParticleClass.spawnParticle(loadedPrefab, collision.GetContact(0).point, Camera.main.transform.rotation);
            AddParticleClass.scaleParticleBasedOnImpactForce(particle, convertedKineticEnergy);
        }
        catch (System.NullReferenceException e)
        {
            Debug.Log(e);
        }
    }

    public float calculateKineticEnergy(float rigidBodyMass, float rigidBodyVelocityMagnitude)
    {
        {
            return 0.5f * rigidBodyMass * Mathf.Pow(rigidBodyVelocityMagnitude, 2);
        }
    }

    private float convertKineticEnergyBasedOnMaximumAllowedNumber(float kineticEnergy)
    {
        if (kineticEnergy > maximumKineticEnergy)
            return maximumKineticEnergy;
        else
            return kineticEnergy/maximumKineticEnergy;
    }
}
