using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Linq;
public class UserSkillUI : MonoBehaviour
{
    public GameObject thirdPersonController;
    public List<GameObject> skillButtonList = new List<GameObject>();
    private Dictionary<string, List<string>> assignedSkillsDict = new Dictionary<string, List<string>>();
    private void Awake()
    {
    }
    // Start is called before the first frame update
    void Start()
    {
        assignedSkillsDict = FindObjectOfType<StoreGlobalData>().assignedSkillsDict;
        for (int i = 0; i < skillButtonList.Count; i++)
        {
            string spritePath = assignedSkillsDict.ElementAt(i).Value[2];
            var loadedImage = Resources.Load<Sprite>(spritePath);
            skillButtonList[i].GetComponent<Image>().sprite = loadedImage;
        }
        
        /*
        skillAttributes = thirdPersonController.GetComponent<SkillAttributes>();
        int i = 0;
        foreach (var skill in skillAttributes.skillList)
        {
            if (skill._isPassive == false)
            {
                skillButtonList[i].GetComponent<Image>().sprite = skill._skillSprite;
                skill.SetKeyCodeForSkillActivation(convertedKeyCodeDict[i]);
                i += 1;
            }
        }
        */
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
