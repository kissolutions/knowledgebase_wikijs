# Pitot Tube Airflow Measurement

## Overview

A **pitot tube** is a device used to measure **air velocity in HVAC
ducts** by comparing **total pressure** and **static pressure**. The
difference between these two pressures is called **velocity pressure**,
which can be converted to **air velocity** and **airflow (CFM)**.

Pitot tubes are widely used for:

-   HVAC Testing, Adjusting, and Balancing (TAB)
-   Air handler commissioning
-   Fan performance verification
-   Diagnosing airflow problems
-   Permanent airflow monitoring when paired with averaging probes and
    BAS transmitters

This page focuses on **practical usage for BAS technicians and controls
engineers**. Detailed airflow sizing calculations are covered in a
separate engineering playbook.

------------------------------------------------------------------------

## Device Classification

Pitot tubes are classified as **airflow measurement devices** used in
HVAC and Building Automation Systems (BAS).

Typical hierarchy:

Airflow Measurement Device\
→ Pitot Tube\
→ Averaging Pitot Probe\
→ Airflow Measurement Station

Pitot tubes themselves **do not generate an electrical signal** and
require a **differential pressure transmitter** or handheld manometer.

------------------------------------------------------------------------

## Purpose in HVAC Systems

Pitot tubes allow technicians to determine:

-   Duct air velocity
-   Total airflow (CFM)
-   Fan airflow performance
-   System airflow balance
-   Air delivery verification

Typical scenarios include:

-   Commissioning HVAC systems
-   Diagnosing airflow issues
-   Verifying VAV airflow
-   Confirming fan airflow output
-   Temporary airflow measurement during troubleshooting

Permanent airflow monitoring systems commonly use **averaging pitot
probes or airflow stations**.

------------------------------------------------------------------------

## How It Works (Practical Explanation)

A pitot tube measures two pressures inside a duct.

  -----------------------------------------------------------------------
  Pressure Type                       Description
  ----------------------------------- -----------------------------------
  Total Pressure                      Pressure of the moving air stream

  Static Pressure                     Pressure inside the duct
                                      independent of airflow velocity

  Velocity Pressure                   Difference between total and static
                                      pressure
  -----------------------------------------------------------------------

Velocity pressure is converted to air velocity:

Velocity = 4005 × √VelocityPressure

Airflow is then calculated:

Airflow (CFM) = Velocity × Duct Area

In BAS systems:

1.  Differential pressure transmitter measures velocity pressure
2.  BAS calculates airflow using duct area and formula

Higher velocity pressure → higher airflow.

------------------------------------------------------------------------

## Device Components

Typical pitot airflow systems include:

### Pitot Probe

Metal probe inserted into airflow.

### Total Pressure Port

Faces upstream into airflow.

### Static Pressure Port

Measures duct static pressure.

### Differential Pressure Transmitter

Converts pressure difference into electrical signal.

### Pneumatic Tubing

Connects probe to transmitter.

### Mounting Hardware

Used to secure probe through duct wall.

------------------------------------------------------------------------

## Types of Pitot Devices

### Single Pitot Tube

Basic probe used for:

-   TAB measurements
-   Duct traverse testing
-   Troubleshooting airflow

### Pitot Traverse Measurement

Multiple readings across the duct to determine average velocity.

Used when higher accuracy is required.

### Averaging Pitot Tube (Multi-Port Probe)

Contains multiple sensing ports along the probe.

Benefits:

-   averages airflow across duct
-   reduces turbulence error
-   supports permanent BAS monitoring

Examples:

-   Annubar probes
-   averaging flow sensors
-   airflow measurement stations

------------------------------------------------------------------------

## Typical Installation Locations

Common locations:

-   Supply air ducts
-   Return air ducts
-   Fan discharge ducts
-   Large trunk ducts

### Good Locations

-   long straight duct sections
-   stable airflow areas

### Poor Locations

Avoid installing near:

-   elbows
-   dampers
-   fan discharge
-   branch takeoffs

Turbulence causes measurement error.

------------------------------------------------------------------------

## Selection Considerations

### Duct Size

Small ducts may allow single probe measurement.

Large ducts often require:

-   duct traverse
-   averaging probe

### Velocity Range

Typical HVAC velocities:

500 -- 4000 FPM

### Velocity Pressure Range

Typical velocity pressure:

0.01 -- 2.0 in.w.c

### Accuracy Requirements

  Application      Accuracy
  ---------------- ----------
  TAB testing      High
  BAS monitoring   Moderate
  Diagnostics      Moderate

### Permanent vs Temporary Measurement

  Use Case                Recommended Device
  ----------------------- ------------------------------------
  Temporary measurement   Single pitot
  Commissioning           Pitot traverse
  Continuous monitoring   Averaging probe or airflow station

------------------------------------------------------------------------

## Installation Guidelines

### Probe Orientation

Total pressure port must face **directly into airflow**.

Incorrect orientation produces major errors.

### Straight Duct Requirements

Upstream:

7--10 duct diameters

Downstream:

3--5 duct diameters

### Probe Depth

Single measurement should reach **duct centerline**.

More accurate results require **duct traverse**.

------------------------------------------------------------------------

## BAS Integration

Pitot tubes connect to **differential pressure transmitters**.

Common outputs:

-   4--20 mA
-   0--10 V
-   BACnet
-   Modbus

BAS calculates airflow using:

-   velocity pressure
-   duct area
-   calibration constants

Permanent installations commonly use **averaging probes +
transmitters**.

------------------------------------------------------------------------

## Controls Programming Considerations

Velocity = 4005 × √VelocityPressure\
CFM = Velocity × DuctArea

### Signal Stability

Velocity pressure signals are small and often noisy.

Common BAS techniques:

-   signal filtering
-   rolling averages
-   minimum airflow thresholds

### Typical Alarms

-   low airflow
-   high airflow
-   transmitter failure
-   signal loss

------------------------------------------------------------------------

## Cost and Pricing Considerations

  Device Type                         Typical Cost
  ----------------------------------- ------------------
  Single pitot tube                   \$30 -- \$150
  Professional TAB probe              \$150 -- \$400
  Averaging pitot probe               \$300 -- \$1200
  Airflow measurement station         \$800 -- \$3000+
  Differential pressure transmitter   \$150 -- \$800

### Factors Increasing Cost

-   multi-port averaging probes
-   stainless steel construction
-   factory calibration
-   large duct sizes
-   integrated transmitters
-   BAS communication protocols

Higher-cost devices typically provide:

-   better accuracy
-   easier installation
-   reduced commissioning time
-   permanent airflow monitoring capability

------------------------------------------------------------------------

## Example Manufacturers and Products

**Note:**\
In a mature version of the knowledge model this section should likely
move to a separate document such as:

HVAC Airflow Measurement Vendors

It is included here temporarily to assist device selection and
engineering design.

### KMC Controls

KMC manufactures **differential pressure transmitters** used with pitot
tubes.

Example product:

KMC DPS Series Differential Pressure Transmitter

Typical features:

-   4--20 mA or 0--10 V output
-   configurable pressure ranges
-   designed for HVAC airflow measurement
-   compatible with BAS controllers

Used with pitot probes to create airflow measurement systems.

### Dwyer Instruments

Common supplier of pitot tubes used for TAB.

Example models:

Dwyer 160 Series Stainless Steel Pitot Tube

Example part numbers:

160-6\
160-12\
160-24

Numbers indicate probe length in inches.

Common uses:

-   duct traverse measurement
-   airflow verification
-   commissioning

### Air Monitor Corporation

Manufacturer of **averaging pitot probes and airflow stations**.

Example:

Air Monitor FAN-E Averaging Probe

Features:

-   multi-port sensing
-   permanent airflow monitoring
-   compatible with BAS pressure transmitters

### Ebtron

Manufacturer of airflow measurement stations.

Example:

Ebtron Gold Series Airflow Station

Characteristics:

-   multi-sensor airflow measurement
-   factory calibrated
-   designed for high accuracy airflow measurement
-   used in hospitals and critical ventilation systems

------------------------------------------------------------------------

## Commissioning and Engineering Mistakes

This section focuses on **real-world mistakes seen during installation
and engineering selection**.

### Installation Mistakes

Probe installed backwards.

Total pressure port must face **into airflow**.

Common symptom:

-   negative airflow
-   very low velocity pressure

------------------------------------------------------------------------

Probe installed in turbulent location.

Symptoms:

-   unstable airflow readings
-   inconsistent BAS values

Avoid locations near:

-   elbows
-   dampers
-   fan discharge

------------------------------------------------------------------------

Insufficient straight duct.

Airflow profile becomes distorted.

Results:

-   large measurement errors

------------------------------------------------------------------------

Tubing reversed.

High and low ports swapped.

Symptoms:

-   negative readings
-   incorrect airflow calculations

------------------------------------------------------------------------

Clogged sensing ports.

Dust or debris blocks ports.

Symptoms:

-   airflow reads near zero

------------------------------------------------------------------------

### Engineering Selection Mistakes

Selecting pressure transmitter with incorrect range.

Velocity pressure in HVAC ducts is often extremely small.

Example mistake:

Selecting transmitter range of

0--10 in.w.c

Actual velocity pressure may be:

0--0.2 in.w.c

Result:

Very poor resolution and inaccurate airflow.

------------------------------------------------------------------------

Using single pitot measurement in large duct.

Airflow distribution across large ducts is uneven.

Result:

Major airflow error.

Proper method:

Use **duct traverse or averaging probe**.

------------------------------------------------------------------------

Ignoring turbulence effects.

Installations near:

-   VAV boxes
-   dampers
-   elbows
-   fan discharge

produce distorted airflow readings.

------------------------------------------------------------------------

Incorrect duct area used in BAS calculation.

Very common programming mistake.

Example:

Engineer uses **nominal duct size instead of internal dimensions**.

Result:

Airflow error of 5--15%.

------------------------------------------------------------------------

Ignoring temperature and density effects in critical systems.

Usually acceptable for comfort HVAC but can matter in:

-   laboratories
-   high altitude locations
-   critical ventilation systems

------------------------------------------------------------------------

## Maintenance

Pitot tubes require minimal maintenance but may experience:

-   dust buildup
-   clogged sensing ports
-   damaged tubing
-   condensation in tubing

Recommended checks:

-   inspect tubing
-   verify probe orientation
-   confirm transmitter calibration

------------------------------------------------------------------------

## Failure Modes

  Failure             Symptom
  ------------------- -----------------------
  Tubing leak         Low airflow
  Clogged probe       Zero reading
  Reversed tubing     Negative pressure
  Transmitter drift   Gradual airflow error

------------------------------------------------------------------------

## Field Technician Tips

-   Always verify probe direction first.
-   Label tubing high/low.
-   Avoid turbulent duct locations.
-   Confirm BAS duct area values.
-   Ensure transmitter pressure range matches expected velocity
    pressure.

------------------------------------------------------------------------

## Related Devices

-   Differential Pressure Transmitter
-   Static Pressure Sensor
-   Airflow Measurement Station
-   VAV Flow Sensor

------------------------------------------------------------------------

## Related Engineering Playbooks

-   Pitot Tube Airflow Measurement Sizing
-   Duct Traverse Procedures
-   HVAC Airflow Calculation Methods
