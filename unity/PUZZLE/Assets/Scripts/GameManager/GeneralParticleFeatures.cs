using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
public class GeneralParticleFeatures : MonoBehaviour
{
	public Camera characterCamera;
	// Start is called before the first frame update
	void Start()
    {
		

	}

    // Update is called once per frame
    void Update()
    {

	}
	public GameObject loadParticleFromPrefab(string prefabPath)
    {
		var loadedObject = (GameObject)Resources.Load(prefabPath);
		return loadedObject;
	}
	public GameObject spawnParticle(GameObject particlePrefab, Vector3 position, Quaternion rotation)
	{
		GameObject particles = (GameObject)Instantiate(particlePrefab, position, rotation);


		particles.SetActive(true);



		ParticleSystem ps = particles.GetComponent<ParticleSystem>();


		if (ps != null)
		{
			var main = ps.main;
			if (main.loop)
			{
				ps.gameObject.AddComponent<CFX_AutoStopLoopedEffect>();
				ps.gameObject.AddComponent<CFX_AutoDestructShuriken>();
			}
		}



		return particles;
	}

	public GameObject AddHitEffect(Vector3 spawnPosition, Quaternion spawnRotation)
    {
		GameObject loadedPrefab = loadParticleFromPrefab("FX/Cartoon FX/CFX Prefabs/Misc/" + "CFX_Poof");
		GameObject particle = spawnParticle(loadedPrefab, spawnPosition, spawnRotation);
		return particle;
	}
	public GameObject AddCollectedGemEffect(Vector3 spawnPosition, Quaternion spawnRotation)
	{
		GameObject loadedPrefab = loadParticleFromPrefab("FX/Cartoon FX/CFX2 Prefabs/Pickup Items/" + "CFX2_PickupHeart");
		GameObject particle = spawnParticle(loadedPrefab, spawnPosition, spawnRotation);
		return particle;
	}

	public void scaleParticleBasedOnImpactForce(GameObject particle, float kineticEnergy)
	{
		particle.transform.localScale = particle.transform.localScale * kineticEnergy;
		/*
		foreach (GameObject go in Selection.gameObjects)
		{
			//Scale Shuriken Particles Values
			ParticleSystem[] systems;
			if (pref_IncludeChildren)
				systems = go.GetComponentsInChildren<ParticleSystem>(true);
			else
				systems = go.GetComponents<ParticleSystem>();

			foreach (ParticleSystem ps in systems)
			{
				ScaleParticleValues(ps, go);
			}

			//Scale Lights' range
			Light[] lights = go.GetComponentsInChildren<Light>();
			foreach (Light light in lights)
			{
				light.range *= ScalingValue;
				light.transform.localPosition *= ScalingValue;
			}
		}
		*/
	}
}
