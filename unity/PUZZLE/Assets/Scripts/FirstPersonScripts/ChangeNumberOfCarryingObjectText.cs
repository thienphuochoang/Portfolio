using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ChangeNumberOfCarryingObjectText : MonoBehaviour
{
    public List<Sprite> imageList = new List<Sprite>();
    private PickUpAndThrowObjects PickUpAndThrowObjectsClass;
    public GameObject defaultLoadingImage;
    public GameObject availableItemImage;
    public GameObject carryingItemImage;
    // Start is called before the first frame update
    void Start()
    {
        PickUpAndThrowObjectsClass = FindObjectOfType<PickUpAndThrowObjects>();
    }

    // Update is called once per frame
    void Update()
    {
        List<GameObject> currentCarryingItemList = new List<GameObject>();
        currentCarryingItemList = PickUpAndThrowObjectsClass.itemList;
        if (currentCarryingItemList.Count == 0)
        {
            defaultLoadingImage.SetActive(true);
            availableItemImage.SetActive(false);
            carryingItemImage.SetActive(false);
        }
        else
        {
            defaultLoadingImage.SetActive(false);
            availableItemImage.SetActive(true);
            carryingItemImage.SetActive(true);
            carryingItemImage.GetComponent<Image>().sprite = imageList[currentCarryingItemList.Count - 1];
        }
    }
}
