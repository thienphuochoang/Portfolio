using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KeepGemsIconInsideMinimap : MonoBehaviour
{
    public GameObject player;
    public float minimapSize;
    // Start is called before the first frame update
    void Start()
    {
}

    // Update is called once per frame
	void LateUpdate()
	{
		Dictionary<GameObject, Sprite> chosenGemDictionary = GetComponent<GenerateGemsRandomly>().chosenGemDictionary;
		// Center of Minimap
		Vector3 centerPosition = player.transform.localPosition;

		foreach (KeyValuePair<GameObject, Sprite> instantiateGemPair in chosenGemDictionary)
        {
			// Distance from the gems to Minimap
			float Distance = Vector3.Distance(instantiateGemPair.Key.transform.position, centerPosition);
			if (Distance > minimapSize)
			{
				// Gameobject - Minimap
				Vector3 fromOriginToObject = instantiateGemPair.Key.transform.position - centerPosition;

				// Multiply by MinimapSize and Divide by Distance
				fromOriginToObject *= minimapSize / Distance;

				// Minimap + above calculation
				instantiateGemPair.Key.transform.GetChild(0).transform.position = centerPosition + fromOriginToObject;
			}
		}
	}
}
