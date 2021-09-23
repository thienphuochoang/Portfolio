using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
public class SkillAttributes : MonoBehaviour
{
    [Serializable]
    public struct KeycodeAndSkillDict
    {
        public KeyCode _keycode;
        public List<string> _skillDataList;
        public Skill _skill;
        public KeycodeAndSkillDict(KeyCode keyCode, List<string> skillDataList, Skill skill) : this()
        {
            _keycode = keyCode;
            _skillDataList = skillDataList;
            _skill = skill;
            SetSkillDataFromListToSkillScriptableObject();
        }
        public void SetSkillDataFromListToSkillScriptableObject()
        {
            _skill.skillName = _skillDataList[0];
            _skill.spritePath = _skillDataList[2];
            if (_skillDataList[3] == "Yes")
                _skill.isPassive = true;
            else
                _skill.isPassive = false;
            _skill.activeTime = float.Parse(_skillDataList[4]);
        }
    }
    public Dictionary<KeyCode, KeycodeAndSkillDict> keyCodeAndSkillDict = new Dictionary<KeyCode, KeycodeAndSkillDict>();
    public List<KeycodeAndSkillDict> keycodeAndSkillList = new List<KeycodeAndSkillDict>();
    public Dictionary<string, List<string>> assignedSkillsDict = new Dictionary<string, List<string>>();
    public List<KeyCode> keycodeList = new List<KeyCode> { KeyCode.Alpha1, KeyCode.Alpha2, KeyCode.Alpha3, KeyCode.Alpha4 };
    private List<KeyCode> activateKeyCodeList = new List<KeyCode>();
    private void Awake()
    {
        assignedSkillsDict = FindObjectOfType<StoreGlobalData>().assignedSkillsDict;
        int i = 0;
        foreach (KeyValuePair<string, List<string>> valueList in assignedSkillsDict)
        {
            var type = Type.GetType(valueList.Value[0]);
            var chosenSkill = (Skill)ScriptableObject.CreateInstance(type);
            KeycodeAndSkillDict slotSkill = new KeycodeAndSkillDict(keycodeList[i], valueList.Value, chosenSkill);
            keycodeAndSkillList.Insert(i, slotSkill);
            keyCodeAndSkillDict.Add(keycodeList[i], slotSkill);
            i += 1;
        }
    }
    void Start()
    {
        foreach (var skill in keycodeAndSkillList)
        {
            switch (skill._skill.state)
            {
                case Skill.SkillState.READY:
                    if (skill._skill.isPassive == true)
                    {
                        skill._skill.Activate(this.gameObject);
                        skill._skill.state = Skill.SkillState.ACTIVE;
                    }
                    else
                        activateKeyCodeList.Add(skill._keycode);
                    break;
            }
        }
    }
    void Update()
    {
        foreach (KeyCode pressedKey in activateKeyCodeList)
        {
            if (Input.GetKeyUp(pressedKey))
            {
                var pressedSkillData = keyCodeAndSkillDict[pressedKey];
                switch(pressedSkillData._skill.state)
                {
                    case Skill.SkillState.READY:
                        pressedSkillData._skill.Activate(this.gameObject);
                        pressedSkillData._skill.state = Skill.SkillState.ACTIVE;
                        break;
                }
            }
        }
        /*
        foreach (var skill in skillList)
        {
            switch (state)
            {
                case SkillState.READY:
                    if (skill.isPassive == false)
                    {
                        if (Input.GetKeyDown(key))
                        {
                            skill.Activate(this.gameObject);
                            state = SkillState.ACTIVE;
                        }
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
        */
    }
}