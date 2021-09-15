using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Linq;
public class GemsUIController : MonoBehaviour
{
    public GameObject winningConditionController;
    private Dictionary<GameObject, Sprite> chosenGemDictionary = new Dictionary<GameObject, Sprite>();
    private List<GameObject> winningConditionItem = new List<GameObject>();
    private CollectGems collectGems;
    private PlayerAttributes playerAttributes;
    private GenerateGemsRandomly generateGemsRandomly;
    private bool DidPlayerJustCollectGem = false;
    // Start is called before the first frame update
    void Start()
    {
        generateGemsRandomly = FindObjectOfType<GenerateGemsRandomly>();
        playerAttributes = FindObjectOfType<PlayerAttributes>();
        collectGems = FindObjectOfType<CollectGems>();
        chosenGemDictionary = GetComponent<GenerateGemsRandomly>().chosenGemDictionary;
        for (int i = 0; i < winningConditionController.transform.childCount; i++)
        {
            if (winningConditionController.transform.GetChild(i).transform.name.Contains("WinningConditionItem"))
            {
                winningConditionItem.Add(winningConditionController.transform.GetChild(i).gameObject);
            }
        }

    }

    // Update is called once per frame
    void Update()
    {
        if (chosenGemDictionary.Count > 0)
        {
            for (int i = 0; i < winningConditionItem.Count; i++)
            {
                winningConditionItem[i].GetComponent<Image>().sprite = chosenGemDictionary.ElementAt(i).Value;
            }
        }
        if (playerAttributes.attributes._collectedGems != 0 && playerAttributes.attributes._collectedGems < generateGemsRandomly.maximumSpawningGems)
        {
            for (int i = 0; i < winningConditionItem.Count; i++)
            {
                if (collectGems.justCollectedGem == chosenGemDictionary.ElementAt(i).Key && winningConditionItem[i].GetComponent<Image>().sprite == chosenGemDictionary.ElementAt(i).Value)
                {
                    winningConditionItem[i].SetActive(false);
                }
            }
        }
    }
}
