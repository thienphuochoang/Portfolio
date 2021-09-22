using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;
using System.Linq;
public class SkillsSelectionActions : MonoBehaviour
{
    public Dictionary<string, List<string>> assignedSkillsDict = new Dictionary<string, List<string>>();
    public List<GameObject> skillSlotList = new List<GameObject>();
    private Dictionary<string, List<string>> skillDataDict = new Dictionary<string, List<string>>();
    public GameObject textObject;
    private int alreadySelectionCount = 0;
    private void Awake()
    {
        
    }
    // Start is called before the first frame update
    void Start()
    {
        skillDataDict = GetSkillFromDatabase.CollectDataSkill();
        if (skillDataDict.Count > 0)
        {
            for (int i = 0; i < skillSlotList.Count; i++)
            {
                EditSkillUI(skillSlotList[i], i);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
    }
    public void AddSelectedSkillToList(GameObject skillSelected)
    {
        if (skillSelected.transform.GetChild(0).gameObject.activeSelf == true)
        {
            if (!assignedSkillsDict.ContainsKey(skillSelected.name))
            {
                List<string> skillAttributeList = skillDataDict[skillSelected.name];
                assignedSkillsDict.Add(skillSelected.name, skillAttributeList);
            }
           
        }
        else
        {
            if (assignedSkillsDict.ContainsKey(skillSelected.name))
            {
                assignedSkillsDict.Remove(skillSelected.name);
            }
        }
    }
    public void BackToMainMenu(GameObject selectSkillUI)
    {
        selectSkillUI.SetActive(false);
    }
    public void EditSkillUI(GameObject selectedSkill, int index)
    {
        selectedSkill.name = skillDataDict.ElementAt(index).Key;
        var loadedImage = Resources.Load<Sprite>(skillDataDict.ElementAt(index).Value[2]);
        selectedSkill.GetComponent<Image>().sprite = loadedImage;
    }
    public void EditSkillDescription(GameObject selectedSkill)
    {
        textObject.GetComponent<Text>().text = skillDataDict[selectedSkill.name][1];
    }
    public void SelectAndUnselectSkills(GameObject skillButton)
    {
        if (alreadySelectionCount == 4)
        {
            if (skillButton.transform.GetChild(0).gameObject.activeSelf == true)
            {
                skillButton.transform.GetChild(0).gameObject.SetActive(false);
                alreadySelectionCount -= 1;
                return;
            }
            return;
        }
        else
        {
            if (skillButton.transform.GetChild(0).gameObject.activeSelf == true)
            {
                skillButton.transform.GetChild(0).gameObject.SetActive(false);
                alreadySelectionCount -= 1;
            }
            else
            {
                skillButton.transform.GetChild(0).gameObject.SetActive(true);
                alreadySelectionCount += 1;
            }
        }
    }
}
