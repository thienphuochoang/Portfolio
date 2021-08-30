using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
public class NWSwingToDestination : NetworkBehaviour
{
    public Camera cameraCharacter;
    public Transform crosshairTransform;
    private float hitRange = 1000f;
    [SerializeField]
    private Animator anim;
    private NetworkAnimator nwAnim;
    public Transform mainCharacterMesh;
    public GameObject anchorObj;
    public Transform leftHandAnchor;
    public Transform anchorChain;
    private Transform anchorOfLeftHandAndObject;
    [SyncVar]
    public GameObject instanceAnchorObj;
    // Start is called before the first frame update
    public override void OnStartAuthority()
    {
        
        /*
        anim = GetComponentInChildren<Animator>();
        nwAnim = this.GetComponent<NetworkAnimator>();
        Transform[] allTransformInAnchor = instanceAnchorObj.GetComponentsInChildren<Transform>();
        foreach (Transform child in allTransformInAnchor)
        {
            if (child.name == "Hall_acnhor.balk")
            {
                anchorChain = child;
            }
        }
        */
    }
    void Start()
    {
        if (!hasAuthority)
        {
            return;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (!hasAuthority)
        {
            return;
        }
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
        nwAnim.SetTrigger("swing");
        //anim.Play("SwingToDestination", 0, 0f);
        //anim.speed = 0f;
    }

    public void EndSwingAnimationAndBackToIdle()
    {
        nwAnim.ResetTrigger("swing");
        nwAnim.SetTrigger("idleTrigger");
    }



    [Command]
    public void CmdCreateAnchorInstance()
    {
        GameObject anchorInstance = Instantiate(anchorObj, leftHandAnchor.position, Quaternion.Euler(0f, 180f, 0f), leftHandAnchor);
        //instanceAnchorObj = Instantiate(anchorObj, this.transform.position, Quaternion.Euler(0f, 180f, 0f), leftHandAnchor);
        //anchorInstance.SetActive(false);
        NetworkServer.Spawn(anchorInstance, connectionToClient);
    }
    /*
    [Command]
    public void CmdCreateAnchorInstance()
    {
        instanceAnchorObj = CreateAnchorInstance();
    }
    */
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
    }

    public void ScaleAnchorBasedOnTime()
    {
        //anchorChain.transform.LookAt(this.transform.position);
        Vector3 anchorAndLeftHandDir = instanceAnchorObj.transform.position - leftHandAnchor.transform.position;
        anchorChain.localScale = new Vector3(anchorChain.localScale.x, anchorChain.localScale.y, anchorAndLeftHandDir.magnitude * 3.6f);
    }
}
