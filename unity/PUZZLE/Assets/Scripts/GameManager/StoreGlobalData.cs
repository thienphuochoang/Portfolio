using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StoreGlobalData : MonoBehaviour
{
    public Dictionary<string, List<string>> assignedSkillsDict = new Dictionary<string, List<string>>();
    private SkillsSelectionActions skillsSelectionActions;
    void Awake()
    {
        DontDestroyOnLoad(this.gameObject);
    }
    // Start is called before the first frame update
    void Start()
    {
        skillsSelectionActions = FindObjectOfType<SkillsSelectionActions>();
    }

    // Update is called once per frame
    void Update()
    {
        assignedSkillsDict = skillsSelectionActions.assignedSkillsDict;
    }
}
