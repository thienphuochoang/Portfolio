using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PickUpAndThrowObjects : MonoBehaviour
{
    private float throwForceMax = 1000f;
    private float chargeSpeed = 750f;
    public float throwForce = 0f;
    public GameObject prepareToThrowObject;
    public List<GameObject> itemList = new List<GameObject>();
    public List<GameObject> thrownItemList = new List<GameObject>();
    public int maximumCarriedObject = 9;
    private float smoothTime = 10.0f;
    public Transform crosshairTransform;
    private Animator anim;
    public Camera cameraCharacter;
    public Transform rightHandObj;
    public Transform mainCharacterMesh;
    public GameObject autoRefillObject;
    private DetectionObjectFeatures DetectionObjectFeaturesClass;
    private PickupableItemFeatures PickupableItemFeaturesClass;
    public string thrownState = "CommonObject";
    //private AutoRefillObjectFeatures AutoRefillObjectFeaturesClass;

    //private DetectCollisionImpact DetectCollisionImpactClass;
    // Start is called before the first frame update
    void Start()
    {
        thrownState = "CommonObject";
        anim = mainCharacterMesh.gameObject.GetComponent<Animator>();
        DetectionObjectFeaturesClass = this.gameObject.GetComponent<DetectionObjectFeatures>();
        PickupableItemFeaturesClass = this.gameObject.GetComponent<PickupableItemFeatures>();
        //AutoRefillObjectFeaturesClass = this.gameObject.GetComponent<AutoRefillObjectFeatures>();
        //DetectCollisionImpactClass = FindObjectOfType<DetectCollisionImpact>();
    }

    // Update is called once per frame
    void Update()
    {
        changeSelectedStateOfObject();
        if (thrownState == "CommonObject")
        {
            // Throw Pickupable and default items
            if (itemList.Count > 0)
            {
                if (itemList.Count < maximumCarriedObject)
                {
                    if (Input.GetKeyDown(KeyCode.E))
                    {
                        prepareToThrowObject = PickupableItemFeaturesClass.PickupObject();
                        if (prepareToThrowObject != null)
                            itemList.Insert(itemList.Count, prepareToThrowObject);
                    }
                }
                if (prepareToThrowObject != null)
                    HoldingObject(prepareToThrowObject);
                if (Input.GetMouseButton(0))
                {
                    rightHandObj.gameObject.SetActive(true);
                    itemList[0].SetActive(true);
                    if (DetectionObjectFeaturesClass.instanceDetectionObject != null)
                        DetectionObjectFeaturesClass.instanceDetectionObject.SetActive(false);

                    HoldingObjectAndPrepareToThrowAnimation();
                    ChangeThrowForceBasedOnMousePressing();
                }
                if (Input.GetMouseButtonUp(0))
                {
                    anim.speed = 1;
                    ThrowObjectAnimation();
                    anim.ResetTrigger("holdingObject");
                    ThrowObject(itemList[0]);
                    throwForce = 0f;
                }
            }
            else
            {
                if (Input.GetKeyDown(KeyCode.E))
                {
                    prepareToThrowObject = PickupableItemFeaturesClass.PickupObject();
                    if (prepareToThrowObject != null)
                        itemList.Insert(0, prepareToThrowObject);
                }
            }
        }
        else if (thrownState == "DetectionObject")
        {
            if (DetectionObjectFeaturesClass.thrownDetectionObject != null)
            {
                DetectionObjectFeaturesClass.RerotateDetectionObject(DetectionObjectFeaturesClass.thrownDetectionObject);
            }
            if (DetectionObjectFeaturesClass.instanceDetectionObject != null)
            {
                // Throw Detection Object
                if (Input.GetMouseButton(0))
                {
                    rightHandObj.gameObject.SetActive(true);
                    DetectionObjectFeaturesClass.instanceDetectionObject.SetActive(true);

                    HoldingObjectAndPrepareToThrowAnimation();
                    ChangeThrowForceBasedOnMousePressing();
                }
                if (Input.GetMouseButtonUp(0))
                {
                    anim.speed = 1;
                    ThrowObjectAnimation();
                    anim.ResetTrigger("holdingObject");
                    DetectionObjectFeaturesClass.ThrowDetectionObject(throwForce);

                    throwForce = 0f;
                }
            }
        }
    }

    void HoldingObject(GameObject o)
    {
        o.transform.SetParent(rightHandObj);
        rightHandObj.gameObject.SetActive(false);
        o.transform.position = Vector3.Lerp(o.transform.position, rightHandObj.position + new Vector3(0, -0.3f ,0), Time.deltaTime * smoothTime);
        o.transform.rotation = Quaternion.identity;
    }

    void ThrowObject(GameObject o)
    {
        o.transform.SetParent(null);
        //isHolding = false;
        o.GetComponent<Rigidbody>().isKinematic = false;
        Vector3 dir = crosshairTransform.transform.forward;
        o.transform.position = crosshairTransform.transform.position;
        o.GetComponent<Rigidbody>().AddForce(dir * throwForce);

        //prepareToThrowObject.AddComponent<PreventGoThroughObjects>();
        o.AddComponent<GeneralParticleFeatures>();
        o.AddComponent<DetectCollisionImpact>();
        

        for (int i = 0; i < itemList.Count; i ++)
        {
            if (itemList[i].name == o.name)
            {
                if (itemList[i].name.Contains("Default_Item"))
                {
                    thrownItemList.Add(itemList[i]);
                }
                itemList.RemoveAt(i);
            }
        }
        if (itemList.Count > 0)
            prepareToThrowObject = itemList[0];
        else
            prepareToThrowObject = null;
    }

    void ChangeThrowForceBasedOnMousePressing()
    {
        if (throwForce > throwForceMax)
        {
            throwForce = throwForceMax;
        }
        else
        {
            throwForce = throwForce + Time.deltaTime * chargeSpeed;
        }
    }

    void ThrowObjectAnimation()
    {
        anim.SetFloat("throwObjectMultiplier", 3.5f);
        anim.SetTrigger("throwObject");
    }

    void HoldingObjectAndPrepareToThrowAnimation()
    {
        anim.SetTrigger("holdingObject");
        anim.Play("HoldingObject", 0, 0f);
        anim.speed = 0f;
    }
    
    void changeSelectedStateOfObject()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            thrownState = "CommonObject";
        }
        else if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            thrownState = "DetectionObject";
        }
    }
}

