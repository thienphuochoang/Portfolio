using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Reflection;

public class TransformIntoAnotherObj : MonoBehaviour
{
    private float hitRange = 30.0f;
    [SerializeField]
    private Transform crosshairTransform;
    [SerializeField]
    private GameObject meshObj;
    [SerializeField]
    private Camera cameraCharacter;
    public GameObject gameManager;
    private GeneralParticleFeatures GeneralParticleFeaturesClass;
    private string objectTag = "Transformable";
    private string playerTag = "Player";
    private string crosshairName = "P_Crosshair";
    private string cameraTag = "PlayerCamera";
    private PlayerAttributes playerAttributes;
    
    // Start is called before the first frame update
    void Start()
    {
        playerAttributes = GetComponent<PlayerAttributes>();
        GeneralParticleFeaturesClass = gameManager.GetComponent<GeneralParticleFeatures>();

        crosshairTransform = RecursiveFindChild(this.transform, crosshairName, "name");

        Transform meshObjTransform;
        meshObjTransform = RecursiveFindChild(this.transform, playerTag, "tag");
        meshObj = meshObjTransform.gameObject;

        Transform cameraTransform;
        cameraTransform = RecursiveFindChild(this.transform, cameraTag, "tag");
        cameraCharacter = cameraTransform.gameObject.GetComponent<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            if (playerAttributes.attributes.IsManaAvailable() == true)
            {
                GameObject rayCastedObj = null;
                rayCastedObj = GetObjectFromRaycast();
                if (rayCastedObj != null)
                {
                    string getObjTag = rayCastedObj.tag;
                    if (getObjTag.Contains(objectTag))
                    {
                        GameObject oldMainCharacter = meshObj;
                        GameObject loadedPrefab = GeneralParticleFeaturesClass.loadParticleFromPrefab("FX/Cartoon FX/CFX Prefabs/Misc/" + "CFX_MagicPoof");
                        GameObject particle = GeneralParticleFeaturesClass.spawnParticle(loadedPrefab, oldMainCharacter.transform.position, Quaternion.Euler(0, 0, 0));

                        GameObject newMainCharacter = null;
                        newMainCharacter = Instantiate(rayCastedObj, oldMainCharacter.transform.position, oldMainCharacter.transform.rotation, oldMainCharacter.transform.parent);
                        newMainCharacter.name = "MainCharacter";
                        newMainCharacter.tag = "Player";
                        newMainCharacter.layer = 2;
                        //if (newMainCharacter.GetComponent<Rigidbody>())
                        //{
                        //newMainCharacter.GetComponent<Rigidbody>().constraints = RigidbodyConstraints.FreezePositionY;
                        //    Destroy(newMainCharacter.GetComponent<Rigidbody>());

                        //}
                        newMainCharacter.transform.rotation = Quaternion.Euler(0, 0, 0);

                        Destroy(oldMainCharacter);
                        meshObj = newMainCharacter;
                        playerAttributes.attributes._mana -= 1;
                    }
                }
            }
        }
    }

    private GameObject GetObjectFromRaycast()
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
    public Transform RecursiveFindChild(Transform parent, string childName, string findType)
    {
        if (findType == "name")
        {
            foreach (Transform child in parent)
            {
                if (child.name == childName)
                {
                    return child;
                }
                else
                {
                    Transform found = RecursiveFindChild(child, childName, findType);
                    if (found != null)
                    {
                        return found;
                    }
                }
            }
            return null;
        }
        else if (findType == "tag")
        {
            foreach (Transform child in parent)
            {
                if (child.tag == childName)
                {
                    return child;
                }
                else
                {
                    Transform found = RecursiveFindChild(child, childName, findType);
                    if (found != null)
                    {
                        return found;
                    }
                }
            }
            return null;
        }
        else return null;
    }

}