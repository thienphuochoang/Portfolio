using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FillDetectionProgressCircle : MonoBehaviour
{
    private DetectionObjectFeatures DetectionObjectFeaturesClass;
    public GameObject detectionLoadingImage;
    public GameObject availableDetectionItemImage;
    private float activeTime = 0f;
    private float maxTime;
    // Start is called before the first frame update
    void Start()
    {
        DetectionObjectFeaturesClass = FindObjectOfType<DetectionObjectFeatures>();
        setDefaultProgressCircleStatus();
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (DetectionObjectFeaturesClass.instanceDetectionObject != null)
        {
            activeTime = 0f;
            setDefaultProgressCircleStatus();
        }
        else
        {
            setLoadingCircleStatus();
            maxTime = DetectionObjectFeaturesClass.replenishDetectionTime;
            activeTime += Time.deltaTime;
            float percent = activeTime / maxTime;
            detectionLoadingImage.GetComponent<Image>().fillAmount = Mathf.Lerp(0, 1, percent);
        }
    }
    void setDefaultProgressCircleStatus()
    {
        availableDetectionItemImage.SetActive(true);
        detectionLoadingImage.SetActive(false);
    }
    void setLoadingCircleStatus()
    {
        availableDetectionItemImage.SetActive(false);
        detectionLoadingImage.SetActive(true);
    }
}
