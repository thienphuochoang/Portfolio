using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UserSkillUI : MonoBehaviour
{
    public GameObject thirdPersonController;
    private SkillAttributes skillAttributes;
    public List<GameObject> skillButtonList = new List<GameObject>();
    private Dictionary<int, KeyCode> convertedKeyCodeDict = new Dictionary<int, KeyCode>();
    private void Awake()
    {
        convertedKeyCodeDict.Add(0, KeyCode.Alpha1);
        convertedKeyCodeDict.Add(1, KeyCode.Alpha2);
        convertedKeyCodeDict.Add(2, KeyCode.Alpha3);
        convertedKeyCodeDict.Add(3, KeyCode.Alpha4);
    }
    // Start is called before the first frame update
    void Start()
    {
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
