using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class HealthAndManaUI : MonoBehaviour
{
    [Header("Player Settings")]
    public GameObject thirdPersonController;
    private PlayerAttributes playerAttributes;
    public GameObject healthImage;
    public GameObject manaImage;
    public List<Sprite> numberImageList = new List<Sprite>();

    // Start is called before the first frame update
    void Start()
    {
        playerAttributes = thirdPersonController.GetComponent<PlayerAttributes>();
    }

    // Update is called once per frame
    void Update()
    {
        int health = playerAttributes.attributes._health;
        int mana = playerAttributes.attributes._mana;
        healthImage.GetComponent<Image>().sprite = numberImageList[health];
        manaImage.GetComponent<Image>().sprite = numberImageList[mana];
    }
}
