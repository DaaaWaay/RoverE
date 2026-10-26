class encoder
{
public:
    encoder(/* args */);
    ~encoder();
};


class pidControll
{
private:
    /* data */
public:
    pidControll(float kP, float kI, float Kd, float minOut, float maxOut);
    ~pidControll();
    float update(float targetState, float currentState, float dt);
};

class motorDriver
{
private:
    /* data */
public:
    motorDriver(float );
    ~motorDriver();
    void set(float pulseSpeed)
};




