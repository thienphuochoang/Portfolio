using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SwingToDestination : MonoBehaviour
{
    public Camera cameraCharacter;
    public Transform crosshairTransform;
    private float hitRange = 1000f;
    private Animator anim;
    public Transform mainCharacterMesh;
    public GameObject anchorObj;
    public Transform leftHandAnchor;
    public Transform anchorChain;
    private Transform anchorOfLeftHandAndObject;
    public GameObject instanceAnchorObj;
    // Start is called before the first frame update
    void Start()
    {
        instanceAnchorObj = CreateAnchorInstance();
        anim = mainCharacterMesh.gameObject.GetComponent<Animator>();
        Transform[] allTransformInAnchor = instanceAnchorObj.GetComponentsInChildren<Transform>();
        foreach (Transform child in allTransformInAnchor)
        {
            if (child.name == "Hall_acnhor.balk")
            {
                anchorChain = child;
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
    }
    public Vector3 GetHitPointFromRaycast()
    {
        Ray ray = cameraCharacter.ScreenPointToRay(cameraCharacter.WorldToScreenPoint(crosshairTransform.position));
        RaycastHit hitObj;

        if (Physics.Raycast(ray, out hitObj, hitRange))
        {
            return hitObj.point;
        }
        else
        {
            return Vector3.zero;
        }
    }
    public GameObject GetObjectFromRaycast()
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
    public void SwingAnimation()
    {
        anim.SetTrigger("swing");
        anim.Play("SwingToDestination", 0, 0f);
        anim.speed = 0f;
    }

    public void EndSwingAnimationAndBackToIdle()
    {
        anim.ResetTrigger("swing");
        anim.SetTrigger("idleTrigger");
    }

    public GameObject CreateAnchorInstance()
    {
        instanceAnchorObj = Instantiate(anchorObj, leftHandAnchor.position, Quaternion.Euler(0f, 180f, 0f), leftHandAnchor);
        //instanceAnchorObj = Instantiate(anchorObj, this.transform.position, Quaternion.Euler(0f, 180f, 0f), leftHandAnchor);
        return instanceAnchorObj;
    }
    public void MoveAnchorToHitPoint(GameObject instanceAnchorObj, Vector3 hitPoint)
    {

        Transform[] allTransformInAnchor = instanceAnchorObj.GetComponentsInChildren<Transform>();
        foreach (Transform child in allTransformInAnchor)
        {
            if (child.name == "Hall_acnhor.balk")
            {
                anchorChain = child;
            }
        }

        float step = 20f * Time.deltaTime;
        instanceAnchorObj.transform.SetParent(null);
        instanceAnchorObj.transform.position = Vector3.MoveTowards(instanceAnchorObj.transform.position, hitPoint, step);



        instanceAnchorObj.transform.LookAt(instanceAnchorObj.transform.position - (hitPoint - instanceAnchorObj.transform.position));
        Vector3 v1 = instanceAnchorObj.transform.position - hitPoint;
        Vector3 v2 = this.transform.position - hitPoint;
        //instanceAnchorObj.transform.LookAt(leftHandAnchor);
        //instanceAnchorObj.transform.localRotation = crosshairTransform.localRotation;
        //Debug.Log(lengthBetweenHitPointAndCharacter);
        //ScaleAnchorBasedOnTime(anchorChain, lengthBetweenHitPointAndCharacter);
        //anchorChain.localScale = new Vector3(anchorChain.localScale.x, anchorChain.localScale.y , lengthBetweenHitPointAndCharacter * 2.7f);
    }

    public void ScaleAnchorBasedOnTime()
    {
        //anchorChain.transform.LookAt(this.transform.position);
        Vector3 anchorAndLeftHandDir = instanceAnchorObj.transform.position - leftHandAnchor.transform.position;
        anchorChain.localScale = new Vector3(anchorChain.localScale.x, anchorChain.localScale.y, anchorAndLeftHandDir.magnitude * 3.6f);
    }

    public static float AngleInRad(Vector3 vec1, Vector3 vec2)
    {
        return Mathf.Atan2(vec2.y - vec1.y, vec2.x - vec1.x);
    }

    //This returns the angle in degrees
    public static float AngleInDeg(Vector3 vec1, Vector3 vec2)
    {
        return AngleInRad(vec1, vec2) * 180 / Mathf.PI;
    }

}
