using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.EventSystems;
public class SetObjectAsButton : MonoBehaviour
{
    public UnityEvent clickButtonEvent = new UnityEvent();
    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        GameObject hoverObj = GetObjectsAsButtons();
        if (hoverObj != null)
        {
            //hoverObj.GetComponent<MeshRenderer>().sharedMaterial.SetFloat("_GlowIntensity", 3f);
            var matList = hoverObj.GetComponent<MeshRenderer>().sharedMaterials;
            foreach (var mat in matList)
            {
                if (mat.name.Contains("menu"))
                {
                    Color glowColor = new Color(1f, 1f, 0f, 1f);
                    mat.SetColor("_GlowColor", glowColor);
                    mat.SetFloat("_GlowIntensity", 3f);
                }
            }
        }
        else
        {
            var matList = GetComponent<MeshRenderer>().sharedMaterials;
            foreach (var mat in matList)
            {
                if (mat.name.Contains("menu"))
                {
                    Color defaultColor = new Color(1f, 1f, 1f, 1f);
                    mat.SetColor("_GlowColor", defaultColor);
                    mat.SetFloat("_GlowIntensity", 1f);
                }
            }
        }
        if (Input.GetMouseButtonUp(0))
        {
            GameObject buttonObj = GetObjectsAsButtons();
            if (buttonObj != null)
            {
                clickButtonEvent.Invoke();
            }
        }
    }
    private GameObject GetObjectsAsButtons()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit) && hit.collider.gameObject == this.gameObject)
        {
            return hit.collider.gameObject;
        }
        return null;
    }
}
