using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AutoRefillObjectFeatures : MonoBehaviour
{
    private float refillItemTime = 6f;
    private float destroyItemTime = 8f;
    public GameObject autoRefillObject;
    public Transform rightHandObj;
    private PickUpAndThrowObjects PickUpAndThrowObjectsClass;
    private List<GameObject> itemList = new List<GameObject>();
    private List<GameObject> thrownItemList = new List<GameObject>();
    private int maximumCarriedObject;
    public GameObject instanceAutoRefillObject;
    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(RefillCarryingObjectOvertime(refillItemTime));
        StartCoroutine(DestroyDefaultItemAfterThrow(destroyItemTime));
        PickUpAndThrowObjectsClass = this.GetComponent<PickUpAndThrowObjects>();
    }

    // Update is called once per frame
    void Update()
    {
        itemList = PickUpAndThrowObjectsClass.itemList;
        thrownItemList = PickUpAndThrowObjectsClass.thrownItemList;
        maximumCarriedObject = PickUpAndThrowObjectsClass.maximumCarriedObject;
    }
    IEnumerator DestroyDefaultItemAfterThrow(float waitTime)
    {
        while (true)
        {
            if (thrownItemList.Count > 0)
            {
                foreach (GameObject o in thrownItemList)
                {
                    Destroy(o, 2f);
                }
            yield return new WaitForSeconds(waitTime);
            }
            else
            {
                yield return null;
            }
        }
    }
    IEnumerator RefillCarryingObjectOvertime(float waitTime)
    {
        while (true)
        {
            if (itemList.Count < maximumCarriedObject)
            {
                instanceAutoRefillObject = GenerateDefaultItemThroughTime();
                PickUpAndThrowObjectsClass.GetComponent<PickUpAndThrowObjects>().itemList.Insert(PickUpAndThrowObjectsClass.GetComponent<PickUpAndThrowObjects>().itemList.Count, instanceAutoRefillObject);
                PickUpAndThrowObjectsClass.GetComponent<PickUpAndThrowObjects>().prepareToThrowObject = instanceAutoRefillObject;
                yield return new WaitForSeconds(waitTime);
            }
            else
            {
                yield return null;
            }
        }
    }
    public GameObject GenerateDefaultItemThroughTime()
    {
        GameObject autoRefillObj = Instantiate(autoRefillObject, rightHandObj.position + new Vector3(0, -0.3f, 0), autoRefillObject.transform.rotation, rightHandObj.transform);
        string randomStringName = "";
        randomStringName = GenerateRandomString();
        autoRefillObj.name = "Default_Item_" + randomStringName;
        if (autoRefillObj.GetComponent<Rigidbody>() == null)
        {
            autoRefillObj.AddComponent<Rigidbody>();
        }
        if (autoRefillObj.GetComponent<Collider>() == null)
        {
            autoRefillObj.AddComponent<BoxCollider>();
        }
        if (autoRefillObj.GetComponent<DetectCollisionImpact>() == null)
        {
            autoRefillObj.AddComponent<DetectCollisionImpact>();
        }
        //if (autoRefillObj.GetComponent<PreventGoThroughObjects>() == null)
        //{
        //    autoRefillObj.AddComponent<PreventGoThroughObjects>();
        //}
        autoRefillObj.GetComponent<Rigidbody>().isKinematic = true;
        autoRefillObj.SetActive(false);
        return autoRefillObj;
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
}
