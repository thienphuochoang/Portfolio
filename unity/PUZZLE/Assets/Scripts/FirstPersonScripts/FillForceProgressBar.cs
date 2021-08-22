using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FillForceProgressBar : MonoBehaviour
{
    private PickUpAndThrowObjects PickUpAndThrowObjectsClass;
    // Start is called before the first frame update
    void Start()
    {
        PickUpAndThrowObjectsClass = FindObjectOfType<PickUpAndThrowObjects>();
        setProgressBarStatus(false);
    }

    // Update is called once per frame
    void Update()
    {
        float currentThrowForce = PickUpAndThrowObjectsClass.throwForce;
        float currentFillAmount = currentThrowForce / 1000;
        if (currentFillAmount > 0f)
        {
            setProgressBarStatus(true);
        }
        
        this.GetComponent<Image>().fillAmount = this.GetComponent<Image>().fillAmount + currentFillAmount * Time.deltaTime;
        if (Input.GetMouseButtonUp(0) || Input.GetMouseButtonUp(1))
        {
            this.GetComponent<Image>().fillAmount = 0.0f;
            setProgressBarStatus(false);
        }
    }

    void setProgressBarStatus(bool status)
    {
        this.transform.gameObject.GetComponent<Image>().enabled = status;
        this.transform.parent.gameObject.GetComponent<Image>().enabled = status;
    }
}
