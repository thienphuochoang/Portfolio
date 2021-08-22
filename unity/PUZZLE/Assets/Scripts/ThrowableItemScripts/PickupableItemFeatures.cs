using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PickupableItemFeatures : MonoBehaviour
{
    public Camera cameraCharacter;
    public Transform crosshairTransform;
    private float hitRange = 3.0f;
    public GameObject mainCharacter;
    private Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        anim = mainCharacter.GetComponent<Animator>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        
    }
    private GameObject GetGameObjectFromRaycast(float hitRange)
    {
        Ray ray = cameraCharacter.ScreenPointToRay(cameraCharacter.WorldToScreenPoint(crosshairTransform.position));
        RaycastHit hitObj;

        if (Physics.Raycast(ray, out hitObj, hitRange))
        {
            return hitObj.collider.gameObject;
        }
        else
        {
            return null;
        }
    }
    public GameObject PickupObject()
    {
        GameObject pickupableObj = null;
        try
        {
            pickupableObj = GetGameObjectFromRaycast(hitRange);
        }
        catch (System.NullReferenceException e)
        {
            Debug.Log(e);
        }
        if (pickupableObj != null && pickupableObj.tag.Contains("Pickupable"))
        {
            PickUpAnimation();
            if (pickupableObj.GetComponent<Rigidbody>() == null)
            {
                pickupableObj.AddComponent<Rigidbody>();
            }
            pickupableObj.GetComponent<Rigidbody>().isKinematic = true;
            pickupableObj.SetActive(false);
            return pickupableObj;
            //if (pickupableObj.GetComponent<Rigidbody>() == null)
            //{
            //    pickupableObj.AddComponent<Rigidbody>();
            //}

            //isHolding = true;

            /*
            if (itemList.Count < maximumCarriedObject)
            {
                GameObject item;
                item = pickupableObj.gameObject;
                item.GetComponent<Rigidbody>().isKinematic = true;
                item.SetActive(false);
                itemList.Insert(0, item);
                prepareToThrowObject = item;
            }
            */
        }
        else
            return null;
    }
    private void PickUpAnimation()
    {
        float currentCameraXRotation = cameraCharacter.transform.localEulerAngles.x;

        if (currentCameraXRotation > 180f && currentCameraXRotation < 360f)
        {
            anim.SetFloat("pickUpFromAboveMultiplier", 3.5f);
            anim.SetTrigger("PickUpFromAbove");
        }
        else if (currentCameraXRotation >= 0 && currentCameraXRotation <= 30f)
        {
            anim.SetFloat("pickUpFromTableMultiplier", 3.5f);
            anim.SetTrigger("PickUpFromTable");
        }
        else if (currentCameraXRotation >= 150 && currentCameraXRotation <= 180f)
        {
            anim.SetFloat("pickUpFromTableMultiplier", 3.5f);
            anim.SetTrigger("PickUpFromTable");
        }
        else if (currentCameraXRotation > 30f && currentCameraXRotation < 150f)
        {
            anim.SetFloat("pickUpFromGroundMultiplier", 3.5f);
            anim.SetTrigger("PickUpFromGround");
        }
    }
}
