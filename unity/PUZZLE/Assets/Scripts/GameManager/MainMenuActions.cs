using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class MainMenuActions : MonoBehaviour
{
    public GameObject selectSkillsUI;
    public void LoadSelectSkillsUI()
    {
        selectSkillsUI.SetActive(true);
    }
    public void StartGame()
    {
        SceneManager.LoadScene(1);
    }
    public void QuitGame()
    {
        Application.Quit();
    }
}
