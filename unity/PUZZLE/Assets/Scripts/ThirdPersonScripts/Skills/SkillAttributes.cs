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

        public KeycodeAndSkillDict(KeyCode keyCode, List<string> skillDataList)
        {
            _keycode = keyCode;
            _skillDataList = skillDataList;
        }
    }
    public List<KeycodeAndSkillDict> keycodeAndSkillList = new List<KeycodeAndSkillDict>();
    public Dictionary<string, List<string>> assignedSkillsDict = new Dictionary<string, List<string>>();
    public List<KeyCode> keycodeList = new List<KeyCode> { KeyCode.Alpha1, KeyCode.Alpha2, KeyCode.Alpha3, KeyCode.Alpha4 };
    private float cooldownTime;
    private float activeTime;
    enum SkillState { READY, ACTIVE, COOLDOWN, NOTAVAILABLE }
    SkillState state = SkillState.READY;

    private void Awake()
    {
        assignedSkillsDict = FindObjectOfType<StoreGlobalData>().assignedSkillsDict;
        int i = 0;
        foreach (KeyValuePair<string, List<string>> valueList in assignedSkillsDict)
        {
            KeycodeAndSkillDict slotSkill = new KeycodeAndSkillDict(keycodeList[i], valueList.Value);
            keycodeAndSkillList.Insert(i, slotSkill);
            i += 1;
        }
    }
    void Start()
    {

        /*
        foreach (var skill in skillList)
        {
            switch (state)
            {
                case SkillState.READY:
                    if (skill.isPassive == true)
                    {
                        skill.Activate(this.gameObject);
                        state = SkillState.ACTIVE;
                    }
                    break;
            }
        }
        */
    }
    void Update()
    {
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