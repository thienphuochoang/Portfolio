using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
public class SkillAttributes : MonoBehaviour
{
    public Dictionary<string, List<string>> skillDict = new Dictionary<string, List<string>>();
    public Skill skill;
    private float cooldownTime;
    private float activeTime;
    public KeyCode key;
    enum SkillState { READY, ACTIVE, COOLDOWN, NOTAVAILABLE}
    SkillState state = SkillState.READY;
    private void Awake()
    {
        skillDict = GetSkillFromDatabase();
    }
    void Update()
    {
        switch(state)
        {
            case SkillState.READY:
                if (skill.isPassive == false)
                {
                    if (Input.GetKeyDown(key))
                    {
                        skill.Activate();
                        state = SkillState.ACTIVE;
                    }
                }
                else
                {
                    skill.Activate();
                    state = SkillState.ACTIVE;
                }
                break;
            case SkillState.ACTIVE:
                if (activeTime > 0)
                {
                    activeTime -= Time.deltaTime;
                }
                else
                {
                    state = SkillState.COOLDOWN;
                    cooldownTime = skill.cooldownTime;
                }
                break;
            case SkillState.COOLDOWN:
                if (cooldownTime > 0)
                {
                    cooldownTime -= Time.deltaTime;
                }
                else
                {
                    state = SkillState.READY;
                }
                break;
        }
    }
    private Dictionary<string, List<string>> GetSkillFromDatabase()
    {
        Dictionary<string, List<string>> skillDataDict = new Dictionary<string, List<string>>();
        StreamReader strReader = new StreamReader(Application.dataPath + "/StreamingAssets" + "/SkillData.csv");
        bool endOfFile = false;
        int firstRow = 0;
        while (!endOfFile)
        {
            string dataString = strReader.ReadLine();
            if (dataString == null)
            {
                endOfFile = true;
                break;
            }
            var dataValues = dataString.Split(',');
            if (firstRow != 0)
            {
                List<string> valueList = new List<string>();
                for (int i = 0; i < dataValues.Length; i++)
                {
                    valueList.Insert(i, dataValues[i].ToString());
                }
                skillDataDict.Add(dataValues[0].ToString(), valueList);
            }
            firstRow += 1;
        }
        return skillDataDict;
    }
    /*
    private StoreGlobalData globalData;
    public List<Skill> skillList = new List<Skill>();
    public class Skill
    {
        public string _skillName;
        public bool _isPassive;
        public Sprite _skillSprite;
        public string _skillFunctionName;
        public KeyCode _pressedKeyCode;
        public Skill(string skillName, Sprite skillSprite, bool isPassive, string skillFunctionName)
        {
            _skillName = skillName;
            _isPassive = isPassive;
            _skillSprite = skillSprite;
            _skillFunctionName = skillFunctionName;
        }
        public void SetKeyCodeForSkillActivation(KeyCode registrationKeyCode)
        {
            _pressedKeyCode = registrationKeyCode;
        }

    }
    public void ActivateSkill(Skill inputSkill)
    {
        Invoke(inputSkill._skillFunctionName, 0.1f);
    }
    private void AddFourHP(Skill inputSkill)
    {
        if (Input.GetKeyDown(inputSkill._pressedKeyCode))
            Debug.Log("Add 4 HP");
    }
    private void Awake()
    {
        globalData = FindObjectOfType<StoreGlobalData>();
        foreach (KeyValuePair<string, List<string>> skillData in globalData.assignedSkillsDict)
        {
            var loadedImage = Resources.Load<Sprite>(skillData.Value[1]);
            var functionName = skillData.Value[3];
            bool isPassive = false;
            if (skillData.Value[2].Contains("Yes"))
            {
                isPassive = true;
            }
            Skill skill = new Skill(skillData.Key, loadedImage, isPassive, functionName);
            skillList.Add(skill);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
    }
    */
}
