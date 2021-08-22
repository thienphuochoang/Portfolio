using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DetectionObjectFeatures : MonoBehaviour
{
    public float replenishDetectionTime = 10f;
    public GameObject detectionObject;
    public GameObject instanceDetectionObject = null;
    public GameObject thrownDetectionObject = null;
    public Transform rightHandObject;
    public Transform crosshairTransform;
    private float destroyItemTime = 7f;
    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(DestroyDetectionObjectAfterThrow(destroyItemTime));
        StartCoroutine(ReplenishDetectionObjectCooldown(replenishDetectionTime));
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private IEnumerator DestroyDetectionObjectAfterThrow(float waitTime)
    {
        while (true)
        {
            if (thrownDetectionObject != null)
            {
                Destroy(thrownDetectionObject, waitTime);
                yield return new WaitForSeconds(waitTime);
            }
            else
            {
                yield return null;
            }
        }
    }
    private IEnumerator ReplenishDetectionObjectCooldown(float waitTime)
    {
        while (true)
        {
            if (instanceDetectionObject == null)
            {
                yield return new WaitForSeconds(waitTime);
                instanceDetectionObject = ReplenishDetectionObject(rightHandObject.position, rightHandObject);
            }
            else
            {
                yield return null;
            }
        }
    }
    private string GenerateRandomString()
    {
        string randomStringName = "";
        const string glyphs = "abcdefghijklmnopqrstuvwxyz";
        int charAmount = Random.Range(5, 8); //set those to the minimum and maximum length of the string
        for (int i = 0; i < charAmount; i++)
        {
            randomStringName += glyphs[Random.Range(0, glyphs.Length)];
        }
        return randomStringName;
    }
    private GameObject ReplenishDetectionObject(Vector3 instantiateLocation, Transform parentObject)
    {
        GameObject detectedObj = Instantiate(detectionObject, instantiateLocation, detectionObject.transform.rotation, parentObject);
        string randomStringName = "";
        randomStringName = GenerateRandomString();
        detectedObj.name = "Detection_Object_" + randomStringName;
        return detectedObj;
    }
    public void ThrowDetectionObject(float throwForce)
    {
        if (instanceDetectionObject.GetComponent<Rigidbody>() == null)
        {
            instanceDetectionObject.AddComponent<Rigidbody>();
        }
        instanceDetectionObject.transform.SetParent(null);
        instanceDetectionObject.GetComponent<Rigidbody>().isKinematic = false;
        Vector3 dir = crosshairTransform.transform.forward;
        instanceDetectionObject.transform.position = crosshairTransform.transform.position;
        instanceDetectionObject.GetComponent<Rigidbody>().AddForce(dir * throwForce);

        //prepareToThrowObject.AddComponent<PreventGoThroughObjects>();
        //instanceDetectionObject.AddComponent<GeneralParticleFeatures>();
        instanceDetectionObject.AddComponent<DetectCollisionImpact>();
        instanceDetectionObject.AddComponent<FindMonstersInRange>();

        thrownDetectionObject = instanceDetectionObject;
        instanceDetectionObject = null;
    }
    public void RerotateDetectionObject(GameObject o)
    {
        Vector3 startDir = o.transform.up;

        Vector3 currentDir = Vector3.Slerp(startDir, Vector3.up, Time.deltaTime * 10f);
        Quaternion tweened = Quaternion.FromToRotation(o.transform.up, currentDir);
        o.transform.localRotation *= tweened;
    }
}
