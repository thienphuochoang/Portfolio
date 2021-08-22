using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class SetStateOfThrownButtons : MonoBehaviour
{
    private PickUpAndThrowObjects PickUpAndThrowObjectsClass;
    private string thrownState = "";
    public GameObject throwDefaultItemSelected;
    public GameObject throwChickenSelected;
    public GameObject throwDefaultItemLoading;
    public GameObject throwChickenLoading;
    // Start is called before the first frame update
    void Start()
    {
        PickUpAndThrowObjectsClass = FindObjectOfType<PickUpAndThrowObjects>();
    }

    // Update is called once per frame
    void Update()
    {
        switchStateOfSeletecButtons();
    }
    private void switchStateOfSeletecButtons()
    {
        thrownState = PickUpAndThrowObjectsClass.thrownState;
        if (thrownState == "CommonObject")
        {
            if (throwDefaultItemLoading.activeSelf == true)
            {
                if (throwChickenLoading.activeSelf == false)
                {
                    PickUpAndThrowObjectsClass.thrownState = "DetectionObject";
                }
            }
            else
            {
                throwDefaultItemSelected.SetActive(true);
                throwChickenSelected.SetActive(false);
            }
        }
        else if (thrownState == "DetectionObject")
        {
            if (throwChickenLoading.activeSelf == true)
                PickUpAndThrowObjectsClass.thrownState = "CommonObject";
            else
            {
                throwDefaultItemSelected.SetActive(false);
                throwChickenSelected.SetActive(true);
            }
        }
    }
}
