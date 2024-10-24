using System;
using System.Collections.Generic;

namespace CRUDDATABASE.DAL;

public partial class QlParameter
{
    public int IdqlParameter { get; set; }

    public string NameDestiny { get; set; } = null!;

    public string NumberFish { get; set; } = null!;

    public string Direction { get; set; } = null!;
}
