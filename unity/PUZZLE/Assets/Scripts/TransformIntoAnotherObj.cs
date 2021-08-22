using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Reflection;

public class TransformIntoAnotherObj : MonoBehaviour
{
    private float hitRange = 30.0f;
    public Transform crosshairTransform;
    private GeneralParticleFeatures GeneralParticleFeaturesClass;
    private GameObject newMainCharacter = null;
    // Start is called before the first frame update
    void Start()
    {
        GeneralParticleFeaturesClass = FindObjectOfType<GeneralParticleFeatures>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            Ray ray = Camera.main.ScreenPointToRay(Camera.main.WorldToScreenPoint(crosshairTransform.position));
            RaycastHit hitObj;

            if (Physics.Raycast(ray, out hitObj, hitRange))
            {
                GameObject rayCastedObj = hitObj.collider.gameObject;
                if (rayCastedObj != null)
                {
                    string getObjTag = rayCastedObj.tag;
                    if (getObjTag.Contains("Transformable"))
                    {

                        GameObject meshObj = null;
                        for (int i = 0; i < this.transform.childCount; i++)
                        {
                            if (this.transform.GetChild(i).gameObject.name == "MainCharacter")
                            {
                                meshObj = this.transform.GetChild(i).gameObject;
                                break;
                            }
                        }
                        GameObject oldMainCharacter = meshObj;

                        GameObject loadedPrefab = GeneralParticleFeaturesClass.loadParticleFromPrefab("FX/Cartoon FX/CFX Prefabs/Misc/" + "CFX_MagicPoof");
                        GameObject particle = GeneralParticleFeaturesClass.spawnParticle(loadedPrefab, oldMainCharacter.transform.position, Quaternion.Euler(0, 0, 0));

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
                    }
                }
            }
        }
        /*
        if (newMainCharacter != null)
        {

            if (newMainCharacter.GetComponent<Rigidbody>())
            {
                newMainCharacter.GetComponent<Rigidbody>().constraints = RigidbodyConstraints.FreezePositionY;
                //    Destroy(newMainCharacter.GetComponent<Rigidbody>());

            }
        }
        */

    }

}