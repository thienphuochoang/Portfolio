using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
public class GetSkillFromDatabase : MonoBehaviour
{
    public Dictionary<string, List<string>> skillDataDict = new Dictionary<string, List<string>>();
    // Start is called before the first frame update
    void Awake()
    {
        skillDataDict = CollectDataSkill();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private Dictionary<string, List<string>> CollectDataSkill()
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
}
