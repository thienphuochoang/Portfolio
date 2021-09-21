using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;
public class PlayerAttributes : MonoBehaviour
{
    public Attributes attributes;
    private GenerateGemsRandomly generateGemsRandomly;
    public UnityEvent assignSkillEvent = new UnityEvent();
    public class Attributes
    {
        public int _health;
        public int _mana;
        public int _collectedGems;
        private int _maximumSpawningGems;
        public Attributes(int health, int mana, int collectedGems, int maximumSpawningGems)
        {
            _health = health;
            _mana = mana;
            _collectedGems = collectedGems;
            _maximumSpawningGems = maximumSpawningGems;
        }
        public bool IsManaAvailable()
        {
            if (_mana == 0)
                return false;
            else
                return true;
        }
        public bool DidCollectAllGems()
        {
            if (_collectedGems == _maximumSpawningGems)
            {
                return true;
            }
            return false;
        }
        public bool IsOutOfHp()
        {
            if (_health == 0)
                return true;
            return false;
        }
    }

    // Start is called before the first frame update
    public void Start()
    {
        generateGemsRandomly = FindObjectOfType<GenerateGemsRandomly>();
        int defaultHP = 5;
        int defaultMana = 5;
        attributes = new Attributes(defaultHP, defaultMana, 0, generateGemsRandomly.maximumSpawningGems);
    }

    // Update is called once per frame
    void Update()
    {
    }
}
